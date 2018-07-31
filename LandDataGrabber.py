import json
from osgeo import ogr
import sys
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = 1000000000

customPoly = [[[40.7743203, -123.1131192], [40.7744149, -123.1130963], [40.774541, -123.113035], [40.7748836, -123.1128446], [40.7751089, -123.1127301], [40.7761723, -123.1123105], [40.7763436, -123.112173], [40.776506, -123.1119289], [40.7766052, -123.1118146], [40.7767765, -123.1116694], [40.7769433, -123.1115552]], [[40.7772092, -123.1113491]], [[40.7552215, -123.1384257], [40.7554961, -123.1385022], [40.7557573, -123.138609], [40.756221, -123.1387541], [40.7564507, -123.1388152], [40.7566804, -123.1388456], [40.756847, -123.138876], [40.7570452, -123.1389293]], [[40.7609944, -123.1397766]], [[40.7659979, -123.1015811], [40.7661333, -123.1012688]], [[40.772458, -123.1432576], [40.7724219, -123.1432575], [40.7723859, -123.1432452], [40.7723138, -123.1432451], [40.7722013, -123.1432089], [40.7721653, -123.1431847], [40.7720932, -123.1431846], [40.7720572, -123.1431604], [40.7719445, -123.1431602], [40.7719085, -123.1431723], [40.7718725, -123.1431723], [40.7718365, -123.1431839], [40.7716923, -123.1431837], [40.7716517, -123.1432077], [40.7715887, -123.1432075], [40.7715256, -123.1431833], [40.7714536, -123.1431831], [40.7714176, -123.1431591], [40.771341, -123.1431589], [40.771305, -123.1431347], [40.771269, -123.1431347], [40.7711969, -123.1431105], [40.7711609, -123.1431103], [40.7711249, -123.1430984], [40.7710889, -123.143062], [40.7710484, -123.1430619], [40.7709763, -123.1430377], [40.7709403, -123.1430136], [40.7709043, -123.1430016]], [[40.7703911, -123.1427361]], [[40.7698555, -123.1423863], [40.7698241, -123.1423498]], [[40.7694597, -123.1419885]], [[40.7651936, -123.1094183]], [[40.7776003, -123.1313799], [40.778829, -123.1303161], [40.7791806, -123.1301256], [40.7797623, -123.1294924]], [[40.787404, -123.1144167]], [[40.7641491, -123.1040074]], [[40.765103, -123.105085], [40.765229, -123.1052833]], [[40.7708694, -123.1180697], [40.7704685, -123.118093], [40.7701577, -123.1181524], [40.7696441, -123.1181275], [40.7693153, -123.1181509], [40.7688065, -123.1180059], [40.7684777, -123.1180295], [40.7678561, -123.1180043], [40.7674146, -123.1180997]], [[40.7711485, -123.149512], [40.7711667, -123.1493061], [40.7711445, -123.1490694], [40.7710863, -123.1487797], [40.771019, -123.148604], [40.7709561, -123.1484895], [40.7708662, -123.1483601], [40.7707763, -123.1481769], [40.7706461, -123.147887], [40.7705382, -123.1477268]], [[40.7767993, -123.140395], [40.7768572, -123.1408833], [40.7769335, -123.1411504], [40.7769963, -123.1413257], [40.7770773, -123.1414325]], [[40.7604201, -123.1128829]], [[40.792567, -123.1221453], [40.7928785, -123.1214969], [40.7931178, -123.1209551]], [[40.7647993, -123.1547361]], [[40.7649302, -123.1545802]], [[40.7649933, -123.154496]], [[40.7651468, -123.1542801], [40.7652145, -123.1541957]], [[40.7652777, -123.1540879]], [[40.7654039, -123.1539437], [40.7655033, -123.1538117]], [[40.7774743, -123.1023385]], [[40.7770641, -123.1026894]], [[40.7756809, -123.1030787]], [[40.7743926, -123.1032159]], [[40.7800824, -123.1118542], [40.7802312, -123.1116141], [40.7803847, -123.1112295]], [[40.7874601, -123.1169343]], [[40.7747885, -123.1086101], [40.7743875, -123.1088161], [40.7741216, -123.1088924], [40.7740225, -123.1089459], [40.7738558, -123.1089993], [40.7737116, -123.1090295], [40.77359, -123.1090449], [40.7732791, -123.1091058], [40.773108, -123.1091059], [40.7728602, -123.109121], [40.77268, -123.1091211], [40.7725314, -123.109106]], [[40.7718963, -123.1091442]], [[40.7716619, -123.1092738]], [[40.7700894, -123.109846]], [[40.7703907, -123.1149654]], [[40.7694308, -123.1154537]], [[40.7688945, -123.1157358], [40.7687368, -123.1157892], [40.7685971, -123.1158427], [40.7684348, -123.115942], [40.7683267, -123.1159952], [40.7679708, -123.1160716], [40.7677816, -123.1160486], [40.767597, -123.115995], [40.7674799, -123.1159496], [40.7673764, -123.1159191], [40.7671646, -123.1159343], [40.7670295, -123.1158962], [40.766908, -123.115835], [40.7667505, -123.1157054]], [[40.7666453, -123.1030554]], [[40.7843584, -123.1104948], [40.7845612, -123.1104721]], [[40.7849485, -123.1105254], [40.7851828, -123.1104721], [40.785435, -123.1104414], [40.7856242, -123.1104261]], [[40.7918797, -123.1403647], [40.7919876, -123.1404868]], [[40.7571722, -123.122091], [40.7572759, -123.122053], [40.7575779, -123.1218545], [40.7577491, -123.1217859], [40.7579925, -123.1216409], [40.7582043, -123.1215417], [40.7583665, -123.1214961], [40.7584971, -123.1214959], [40.7586908, -123.1215418], [40.7588889, -123.1216029], [40.759069, -123.1216487], [40.7592086, -123.1216943], [40.7593618, -123.1216945], [40.7595104, -123.1217403], [40.75983, -123.1218853], [40.75992, -123.121931], [40.7600371, -123.1220148], [40.7601856, -123.1221292], [40.7603566, -123.1222513], [40.7605051, -123.1223812], [40.7606627, -123.1224803], [40.7607842, -123.1225793], [40.7610003, -123.1227093], [40.7611848, -123.1228008], [40.7613649, -123.1228696]], [[40.7687101, -123.1573305], [40.7687191, -123.1572703], [40.7687553, -123.1571862], [40.7687915, -123.1570782], [40.7688006, -123.1570301], [40.7688277, -123.1569821], [40.7688548, -123.1568859], [40.7689226, -123.1567538], [40.7689587, -123.1566698], [40.7689768, -123.1566095], [40.7689948, -123.1565737], [40.769013, -123.1565015], [40.7690492, -123.1564175], [40.7690853, -123.1563091], [40.7691034, -123.1562732], [40.7691215, -123.1562252], [40.7691666, -123.1561411], [40.7691847, -123.1560809], [40.7692344, -123.1559851], [40.7692525, -123.155937], [40.7692795, -123.1559007], [40.7693248, -123.1557809], [40.7693428, -123.1557447], [40.7693519, -123.1556847], [40.76937, -123.1556366], [40.769379, -123.1555885], [40.7693971, -123.1555404], [40.7694152, -123.1555046], [40.7694243, -123.1554442], [40.7694424, -123.1553961], [40.7694515, -123.155348], [40.7694695, -123.1553002], [40.7694786, -123.1552521], [40.7695011, -123.1552041], [40.7695554, -123.1551079], [40.7695645, -123.1550599], [40.7695825, -123.1550239], [40.7696006, -123.1549635], [40.7696097, -123.1549155], [40.7696367, -123.1548674], [40.7696549, -123.1547715], [40.7696911, -123.1546994], [40.7697272, -123.1545914], [40.7697634, -123.1545071], [40.7697905, -123.154459], [40.7698221, -123.1543868], [40.7698763, -123.1542789], [40.7699033, -123.1542308], [40.7699305, -123.1541586], [40.7699485, -123.1541228], [40.7699848, -123.1540147], [40.7699849, -123.1539543], [40.7700029, -123.1539184], [40.7700211, -123.1538103], [40.7700213, -123.1536659], [40.7700393, -123.1536301], [40.7700574, -123.1535697], [40.7700575, -123.1535217], [40.7700938, -123.1533295], [40.7700938, -123.1532815], [40.7701029, -123.1532333], [40.7700939, -123.1531851], [40.770094, -123.153137], [40.7701348, -123.1529449], [40.770135, -123.1528005], [40.7701441, -123.1527524], [40.7701441, -123.1527043], [40.7701622, -123.1526561], [40.7701625, -123.1525117], [40.7701715, -123.152464], [40.7701715, -123.1524158], [40.7701806, -123.1523677], [40.7701987, -123.1523196], [40.7701988, -123.1522715], [40.7702079, -123.1522233], [40.7702079, -123.1521753], [40.7702259, -123.1521271], [40.770226, -123.152079], [40.7702441, -123.1520432], [40.7702442, -123.1519831], [40.7702623, -123.1519469], [40.7702623, -123.1518869], [40.7702804, -123.1518507], [40.7702894, -123.1518025], [40.7703075, -123.1517427], [40.7703437, -123.1516464], [40.7703709, -123.1515984], [40.7703799, -123.1515502], [40.7704341, -123.1514063]], [[40.7868679, -123.1051162]], [[40.7882196, -123.104666], [40.788598, -123.1045211], [40.7887692, -123.1044828], [40.7892063, -123.1042998], [40.7893415, -123.1042311], [40.7893776, -123.10417], [40.7895309, -123.1040554], [40.7896751, -123.103926]], [[40.7731149, -123.1576417]], [[40.7731914, -123.1576659]], [[40.7734796, -123.1577148]], [[40.7738489, -123.1578115]], [[40.7741775, -123.1578846]], [[40.7743937, -123.1579573]], [[40.7744702, -123.1579815], [40.7745422, -123.1579817]], [[40.7747628, -123.1580785], [40.7748349, -123.1581027], [40.7748708, -123.1581269]], [[40.7749429, -123.1581512]], [[40.7751275, -123.1581757]], [[40.7756771, -123.1581888]], [[40.7757852, -123.158165]], [[40.7762583, -123.1580458]], [[40.7763349, -123.1580101]], [[40.776407, -123.1579739]], [[40.7766278, -123.1579267]], [[40.7769927, -123.1579276]], [[40.7770647, -123.1579396]], [[40.7775421, -123.1579289]], [[40.7776503, -123.1579169]], [[40.7777224, -123.1579053]], [[40.7780154, -123.1577015]], [[40.7781825, -123.1574612]], [[40.7782907, -123.1573292]], [[40.7907634, -123.1239459], [40.7906462, -123.1240298], [40.7905425, -123.1240833], [40.7904164, -123.1241139], [40.7902812, -123.1241595], [40.7900738, -123.1243195]], [[40.7895095, -123.1254793]], [[40.7377613, -123.2066623], [40.737644, -123.2063111], [40.7373517, -123.2056579], [40.7369039, -123.2050239], [40.7366639, -123.2046311], [40.7364027, -123.2040732], [40.7356918, -123.2024996], [40.7355543, -123.2024392], [40.735367, -123.2021098], [40.7353134, -123.2018805], [40.7352758, -123.2017645], [40.7351787, -123.2015006], [40.7351521, -123.2012227], [40.7351475, -123.2007667], [40.7349534, -123.2001535], [40.7347274, -123.1992623], [40.7346198, -123.1988204], [40.7346111, -123.1982613], [40.7346051, -123.1978799], [40.7346816, -123.1975097], [40.7346121, -123.1969894], [40.7346833, -123.1965338], [40.7347597, -123.1962062], [40.7348592, -123.1957406], [40.7350184, -123.1954112], [40.7350049, -123.19496], [40.7350119, -123.1948649], [40.7350194, -123.1948523], [40.73513, -123.1946664], [40.7354425, -123.1937831]], [[40.7386345, -123.1878838], [40.7386981, -123.1873711], [40.7386571, -123.1866967], [40.7387844, -123.1859898], [40.7390457, -123.1855705], [40.7393404, -123.1852508], [40.7398031, -123.1850973], [40.7406955, -123.1843261], [40.741613, -123.1835107], [40.742135, -123.1830701], [40.7421793, -123.1830163], [40.7425983, -123.1825076], [40.7427419, -123.1822152], [40.742826, -123.182044], [40.7429669, -123.18169], [40.7431467, -123.1812491], [40.7432312, -123.180984], [40.7434502, -123.1806641], [40.7437454, -123.180079], [40.743864, -123.1795378], [40.7440583, -123.178875], [40.7440683, -123.1788199], [40.7442279, -123.1779471], [40.7442371, -123.1774752], [40.7442135, -123.1767362], [40.7442763, -123.176013], [40.744307, -123.1756593], [40.7446778, -123.1750633], [40.7450407, -123.1745421], [40.7455118, -123.1739712], [40.7458008, -123.1734775], [40.7460933, -123.1729779], [40.746272, -123.1726881], [40.7469782, -123.1715432], [40.747046, -123.1711786], [40.7471558, -123.1708141], [40.7473832, -123.1705715], [40.7477537, -123.1701193], [40.7486472, -123.1685408], [40.749262, -123.1677796], [40.749864, -123.167115], [40.7503207, -123.1666783], [40.7507291, -123.1661065], [40.7511373, -123.165627], [40.7512644, -123.1652393], [40.751434, -123.1645373], [40.7515332, -123.1640017], [40.7516181, -123.1635953], [40.7515879, -123.1633375], [40.7514514, -123.162172], [40.7513826, -123.1611185], [40.751313, -123.1606748], [40.7512863, -123.1596213], [40.7518359, -123.1585323], [40.7519922, -123.1583422], [40.7524272, -123.1578129], [40.7543264, -123.1563944], [40.7549031, -123.1559892], [40.7556354, -123.1549005]], [[40.7569337, -123.1508191], [40.7570891, -123.1501541], [40.757132, -123.1496367], [40.7571045, -123.1491469], [40.7576394, -123.1485012], [40.758427, -123.1480594], [40.7588346, -123.1480419], [40.7596917, -123.1481731]], [[40.7623217, -123.1466634]], [[40.7853965, -123.1340628], [40.7853068, -123.1337041], [40.7852035, -123.1334369], [40.7850913, -123.1331167], [40.7850464, -123.1330021], [40.7848531, -123.1326205], [40.7846869, -123.132262]], [[40.768295, -123.1475535], [40.7682636, -123.1475053], [40.7682637, -123.1474571]], [[40.7681739, -123.1472406]], [[40.768111, -123.147072], [40.768093, -123.1470239], [40.7680841, -123.1469757]], [[40.7679541, -123.1464463]], [[40.7679363, -123.14635], [40.7679183, -123.1463022], [40.7679093, -123.1462541], [40.7679095, -123.1462059], [40.7678915, -123.1461577], [40.7678735, -123.1460614], [40.7678556, -123.1460132], [40.7678557, -123.1459651]], [[40.7678197, -123.1458928], [40.7678198, -123.1458447], [40.7678108, -123.1458088], [40.7677839, -123.1457727], [40.7677839, -123.1457365], [40.767703, -123.1455682], [40.7676941, -123.1455079]], [[40.7676357, -123.1453755]], [[40.7675458, -123.1452191], [40.7675279, -123.1451709], [40.7675099, -123.1451586]], [[40.7674379, -123.1450626]], [[40.7673345, -123.144942]], [[40.7668797, -123.1447847]], [[40.7667717, -123.1447723]], [[40.7665149, -123.1447357], [40.7664879, -123.1447357]], [[40.7828589, -123.1101364]], [[40.7809849, -123.1149655]], [[40.7830134, -123.113371]], [[40.7777559, -123.099714], [40.7776072, -123.0998131], [40.7774989, -123.0999888], [40.7773591, -123.1001641], [40.7771518, -123.100309], [40.7769265, -123.100416]], [[40.784192, -123.1003856], [40.7843361, -123.1004163], [40.7850342, -123.1005306], [40.7851873, -123.100546]], [[40.7701838, -123.1275541]], [[40.7731793, -123.1274932], [40.7734542, -123.1273561], [40.7737923, -123.1271193], [40.7741438, -123.1269363], [40.774297, -123.1269514], [40.7744726, -123.1269363], [40.7746527, -123.1270051], [40.7748823, -123.1271499], [40.7749903, -123.1272109], [40.7751567, -123.1274245], [40.7753141, -123.1277299], [40.775717, -123.1290278]], [[40.7739191, -123.1134317], [40.7737432, -123.1136225], [40.7735944, -123.1138059], [40.7734366, -123.1139357], [40.7733194, -123.1140498], [40.7732743, -123.1141109], [40.7730624, -123.1142787], [40.7729407, -123.1143855]], [[40.7810507, -123.1022052]], [[40.7871971, -123.1186206]], [[40.7798093, -123.1191795]], [[40.7824401, -123.1188476]], [[40.7730756, -123.1465442], [40.7729766, -123.14643], [40.7728146, -123.146346], [40.772648, -123.1463], [40.7724048, -123.1463002], [40.7721885, -123.1463535], [40.7720353, -123.1463536], [40.7719002, -123.1463306], [40.7718237, -123.1463001], [40.7717067, -123.1462161], [40.7714503, -123.1459644], [40.7712253, -123.1457355], [40.7710319, -123.1455751], [40.7708924, -123.1454303], [40.7707169, -123.1453007], [40.770528, -123.1451096], [40.7703301, -123.1448429], [40.7701457, -123.1446137], [40.7700423, -123.1444535], [40.769975, -123.1442704], [40.7698672, -123.1440417], [40.7697009, -123.1437366]], [[40.7766098, -123.1404883], [40.7765105, -123.1406685], [40.7764743, -123.1407165], [40.7764653, -123.1407646], [40.7764111, -123.1408608], [40.7764021, -123.1409089], [40.776366, -123.1409569], [40.7763299, -123.1410533], [40.7763028, -123.1411009], [40.7762937, -123.1411491], [40.7762711, -123.1411971], [40.776262, -123.1412452], [40.776262, -123.1412935], [40.7762439, -123.1413897], [40.7762438, -123.1414378], [40.7762257, -123.1414859], [40.7762257, -123.1415341], [40.7762166, -123.1415817], [40.7761985, -123.1416299], [40.7761985, -123.141678], [40.7761894, -123.1417262], [40.7761893, -123.1417743], [40.7761712, -123.1418225], [40.7761622, -123.1418705], [40.7761621, -123.1419187]], [[40.7760896, -123.1423033]], [[40.7760624, -123.1423995]], [[40.7760263, -123.1424957]], [[40.7760172, -123.1425916]], [[40.7759945, -123.1426879]], [[40.7758139, -123.1430723], [40.7757597, -123.1431684], [40.7757416, -123.1432165], [40.7757055, -123.1432523], [40.7757055, -123.1432887], [40.7756649, -123.1433245], [40.7756378, -123.1433607], [40.7756107, -123.1434088], [40.7755656, -123.1434569], [40.7755205, -123.1434927], [40.7755115, -123.1435285], [40.7754755, -123.1435767], [40.7754303, -123.1436247], [40.7754033, -123.1436728], [40.7753627, -123.1437207], [40.7753445, -123.1437689], [40.7753175, -123.1438048], [40.7752995, -123.143841], [40.7752451, -123.1439849], [40.7752181, -123.1440331], [40.7752, -123.1440811], [40.775227, -123.1441175], [40.7752269, -123.1441535], [40.7751999, -123.1442015], [40.7751818, -123.1442496], [40.7751727, -123.1442977], [40.7751547, -123.1443458], [40.7751456, -123.144394], [40.7751275, -123.1444417], [40.7751274, -123.1444898], [40.7750732, -123.1446341], [40.7750641, -123.1446823], [40.7750416, -123.1447303], [40.7750325, -123.1447784], [40.7750145, -123.1448265], [40.7749963, -123.1449225], [40.7749782, -123.1449706], [40.7749601, -123.1450667], [40.7749599, -123.1451631]], [[40.7749327, -123.1453556]], [[40.7749145, -123.1454515]], [[40.794568, -123.1025298], [40.7944733, -123.1026822], [40.7941305, -123.1031936], [40.7940222, -123.1033842], [40.793747, -123.1038494], [40.7935981, -123.1041548]], [[40.7931238, -123.1056731], [40.793038, -123.1059097], [40.7929703, -123.1060241], [40.7928621, -123.1061691], [40.7927223, -123.1063214], [40.792524, -123.1065123], [40.7923662, -123.1066039], [40.791672, -123.1071913], [40.7914195, -123.1074506], [40.7912257, -123.1076644], [40.7910452, -123.1079545], [40.7909144, -123.1081528], [40.7907566, -123.1082822]], [[40.7939703, -123.1358941], [40.7939343, -123.1358699], [40.7938983, -123.1358576], [40.7938578, -123.1358216], [40.7937138, -123.1357251], [40.7936778, -123.1356768], [40.7935697, -123.1356043], [40.7935293, -123.1355683], [40.7934933, -123.1355442], [40.7934573, -123.1355078], [40.7932773, -123.1353873], [40.7932007, -123.1353632], [40.7931647, -123.1353389], [40.7929845, -123.1353386], [40.7929485, -123.1353626], [40.7928719, -123.1353625], [40.7928358, -123.1353865], [40.7927998, -123.1353863], [40.7927277, -123.1354341], [40.7926917, -123.1354463], [40.7926645, -123.1354702], [40.7925789, -123.1355059], [40.7923986, -123.1356259], [40.7923625, -123.1356741], [40.7923265, -123.1357099], [40.7922499, -123.135782], [40.7922137, -123.135806], [40.7921867, -123.1358423], [40.7921416, -123.1358903], [40.7921055, -123.1359139], [40.7920784, -123.135962], [40.7920333, -123.1359982], [40.7919657, -123.1360823], [40.7919297, -123.1361184], [40.7918393, -123.1362505], [40.7917942, -123.1363467], [40.7917761, -123.1363945], [40.791722, -123.1364906], [40.7916453, -123.1365868], [40.7916273, -123.1366349], [40.7916002, -123.136683], [40.7915641, -123.1367311], [40.791537, -123.1367792], [40.7915009, -123.1368151], [40.7914919, -123.1368513], [40.7914377, -123.1369231], [40.7914196, -123.1369711], [40.791379, -123.1370193], [40.7913339, -123.1370555], [40.7913159, -123.1370795], [40.7912437, -123.1371512], [40.7912077, -123.1371753]], [[40.7714845, -123.1400686]], [[40.7714035, -123.1399844], [40.7713855, -123.1399481]], [[40.7710435, -123.1396108]], [[40.7707063, -123.1391291]], [[40.7706525, -123.1389246]], [[40.7706715, -123.138107]], [[40.7703255, -123.1374931], [40.7702714, -123.1374567]], [[40.7701634, -123.1373602]], [[40.770015, -123.1372277]], [[40.7673383, -123.1489221]], [[40.7673115, -123.148838]], [[40.7671865, -123.1480079]], [[40.7671685, -123.1479116]], [[40.7669849, -123.1470936]], [[40.766967, -123.1469973]], [[40.7668953, -123.1467087]], [[40.7668235, -123.1465282], [40.7667965, -123.1464919], [40.7667875, -123.146456], [40.7667605, -123.1464319]], [[40.7667021, -123.1463231], [40.7666841, -123.1462755]], [[40.7666122, -123.1461549]], [[40.7665224, -123.1459743], [40.7665043, -123.1459502]], [[40.7661672, -123.1454685]], [[40.7660728, -123.145324], [40.7660458, -123.1452998]], [[40.7636037, -123.1529058]], [[40.7637434, -123.1527976]], [[40.7641086, -123.1525219]], [[40.7641808, -123.1524621], [40.7642168, -123.1524381]], [[40.7642935, -123.1523783]], [[40.795071, -123.13829], [40.7949628, -123.1383621], [40.7949358, -123.1383861], [40.7948997, -123.1384101], [40.7948096, -123.1384459], [40.7946969, -123.1385179], [40.7946609, -123.1385177], [40.7945887, -123.1385658], [40.7945527, -123.1385775], [40.7945256, -123.1386137], [40.7944761, -123.1386378], [40.79444, -123.1386377]], [[40.7943679, -123.1386616], [40.7943318, -123.1386855], [40.7942959, -123.1386855], [40.7942597, -123.1387095], [40.7941967, -123.1387335]], [[40.7941201, -123.1387574], [40.794075, -123.1387573], [40.7940389, -123.1387809], [40.794003, -123.1387809], [40.7939669, -123.1388049], [40.7939308, -123.1388047], [40.7938948, -123.1388169], [40.7938632, -123.1388409], [40.7938361, -123.1388527], [40.7937461, -123.1388765], [40.79371, -123.1388765], [40.7936379, -123.1389004], [40.7935659, -123.1389003], [40.7935253, -123.1389125], [40.7934893, -123.1389124], [40.7934532, -123.1389241], [40.7933451, -123.1389239], [40.7933091, -123.1389361], [40.7931965, -123.1389358], [40.7931244, -123.1389598], [40.7929037, -123.1389593], [40.7928766, -123.1389711], [40.7927235, -123.1389708], [40.7926874, -123.138983], [40.7926108, -123.1389827], [40.7925748, -123.1389945], [40.7925388, -123.1389945], [40.7925027, -123.1390185], [40.7924667, -123.1390184], [40.7923945, -123.1390423], [40.7923225, -123.1390422], [40.7922459, -123.1390661], [40.7920297, -123.1390656], [40.7919892, -123.1390415], [40.7919172, -123.1390413], [40.7918451, -123.1390171], [40.791773, -123.139017], [40.7917369, -123.1390287], [40.7916964, -123.1390167], [40.7916334, -123.1390408]], [[40.7923411, -123.1184756]], [[40.763259, -123.1387175], [40.7633018, -123.1381816], [40.7633728, -123.1376273]], [[40.766677, -123.1363217], [40.7678713, -123.1364905], [40.7684196, -123.1363622], [40.7688275, -123.1360673], [40.7690386, -123.1358829], [40.7692621, -123.1357939], [40.7693619, -123.1357542], [40.769433, -123.1350889], [40.7691248, -123.1342564], [40.7687037, -123.1338304], [40.768479, -123.1337005], [40.7676922, -123.1334586], [40.7670041, -123.1329766], [40.7666532, -123.1325878], [40.7662606, -123.1317922], [40.7662055, -123.1308124], [40.7665577, -123.1300368], [40.7676689, -123.1292255], [40.7681753, -123.1287459], [40.7683588, -123.1280808], [40.7685145, -123.127083], [40.7686414, -123.1267505], [40.7692035, -123.1267516], [40.7697936, -123.1268821], [40.7701169, -123.1268272], [40.7702324, -123.1261427], [40.7702381, -123.1255781], [40.7700761, -123.1249559], [40.7692441, -123.123209], [40.7689274, -123.1229944], [40.7684821, -123.1226926], [40.7679792, -123.1220891], [40.7672866, -123.1204323], [40.7669402, -123.1196134], [40.7664777, -123.1191559], [40.7662067, -123.1186383], [40.766059, -123.118356], [40.7660018, -123.1177279], [40.765959, -123.1171569], [40.7659159, -123.1167763], [40.7659454, -123.1161674], [40.7660039, -123.1155967], [40.766062, -123.1154065], [40.7661925, -123.1150072], [40.7665476, -123.1141885], [40.7666131, -123.1140375], [40.7666136, -123.1135807], [40.7665255, -123.1132097], [40.766383, -123.1126099], [40.766225, -123.1114489], [40.7661965, -123.1109351], [40.7658506, -123.1096026], [40.7657789, -123.1089554], [40.7659678, -123.1081185], [40.766099, -123.1070151], [40.7660573, -123.1050931], [40.7658843, -123.104465], [40.7657255, -123.1040651], [40.7650245, -123.1033472], [40.7649161, -123.1032361], [40.7640776, -123.1024356], [40.7627913, -123.1009496], [40.7623144, -123.1004161], [40.7612006, -123.1002432], [40.7606511, -123.0998618], [40.760044, -123.0992519], [40.7595383, -123.0984712], [40.7592496, -123.0977477], [40.7592316, -123.0972771], [40.7592213, -123.0970056], [40.7591928, -123.096511], [40.7589182, -123.0962441], [40.7584265, -123.0958249], [40.758398, -123.0953111], [40.7590639, -123.0947984], [40.7596285, -123.0944377], [40.7603086, -123.0943435], [40.7608438, -123.0944204], [40.7616101, -123.0948971], [40.7620147, -123.0955827], [40.7624626, -123.0963635], [40.76307, -123.0966307], [40.7637354, -123.0966507], [40.7652548, -123.0963866], [40.7655879, -123.0958542], [40.7659384, -123.0918968], [40.7656518, -123.0883382], [40.7655956, -123.0861309], [40.7657846, -123.0848467], [40.7655399, -123.0831338], [40.7655109, -123.0830295], [40.7650493, -123.0813635], [40.764616, -123.0803736], [40.7637061, -123.0780131], [40.7629846, -123.0752152], [40.7621187, -123.0717512], [40.7620466, -123.0714087], [40.7619456, -123.071009], [40.7615989, -123.0702286], [40.7604712, -123.0687813], [40.7594303, -123.0675245], [40.7586349, -123.0671431], [40.7582588, -123.0669716], [40.7577524, -123.067028], [40.7572024, -123.0675031], [40.7567533, -123.0685301], [40.7563333, -123.0692336], [40.7559278, -123.0698039], [40.7555949, -123.0700509], [40.7551609, -123.0701265], [40.7545389, -123.0699356], [40.7539459, -123.0696496], [40.7534108, -123.0692305], [40.752847, -123.0686022], [40.752081, -123.0674219], [40.7517197, -123.0666795], [40.751532, -123.0660136], [40.751142, -123.0648717], [40.750535, -123.0637297], [40.7498639, -123.0631405], [40.7492254, -123.0626624], [40.7487025, -123.0624186]], [[40.7481068, -123.0628253], [40.7477361, -123.0639782], [40.747293, -123.0647925], [40.7472043, -123.0651204], [40.7471719, -123.0655966], [40.747059, -123.0660197], [40.7467932, -123.0664215], [40.7456663, -123.0670446], [40.7454652, -123.0670126], [40.7451917, -123.0668324], [40.7444276, -123.0661546], [40.7439531, -123.065752], [40.7431085, -123.0651694], [40.7428511, -123.0649999], [40.7416925, -123.0646284], [40.741065, -123.0644903], [40.7407932, -123.0643328], [40.7404617, -123.0641406], [40.7395769, -123.0634521], [40.7388854, -123.0625734]], [[40.7336589, -123.0549362], [40.7333289, -123.0551476], [40.7329907, -123.055507], [40.7323708, -123.0561306], [40.7322214, -123.0562059], [40.7319361, -123.0565109], [40.7317265, -123.057431], [40.7315246, -123.0588695], [40.7311943, -123.0594933], [40.7311378, -123.0599057], [40.7309362, -123.0606248], [40.7306946, -123.0609949], [40.7300184, -123.0615443], [40.7295355, -123.0618083], [40.7289802, -123.0619559], [40.7286663, -123.0619873], [40.7279501, -123.0620184], [40.7279186, -123.0619942], [40.7277103, -123.0618342], [40.7272584, -123.0614783], [40.7268014, -123.0602331], [40.7266798, -123.0599017]], [[40.7267386, -123.0551263], [40.7262883, -123.0542797], [40.7259908, -123.0539199], [40.7253873, -123.0538136], [40.7245104, -123.0532734], [40.7237625, -123.0524691], [40.7232077, -123.051411], [40.7227335, -123.0501202], [40.7220499, -123.049263], [40.7215512, -123.0487762], [40.7212138, -123.0474221], [40.7211744, -123.047154], [40.7210614, -123.0463856], [40.7209328, -123.045899], [40.7209331, -123.0452327], [40.7211105, -123.0442175], [40.721336, -123.0438686], [40.7212639, -123.0427897], [40.7210874, -123.0414359], [40.7211197, -123.0409811], [40.7207819, -123.0405156], [40.7205084, -123.0401875], [40.7200981, -123.040145], [40.7190116, -123.0406414], [40.718247, -123.0412437], [40.7178928, -123.0415608], [40.7176595, -123.0418523], [40.7176432, -123.0418727], [40.7171763, -123.0424435], [40.7163498, -123.0437278], [40.7159927, -123.0442828], [40.7149219, -123.0459954], [40.7144228, -123.0462594], [40.7131592, -123.0468613], [40.712821, -123.0469151], [40.711936, -123.047056], [40.7115014, -123.0471298], [40.7103507, -123.0472982], [40.7096777, -123.0475549], [40.7094654, -123.0476359], [40.7080569, -123.0483751], [40.7076385, -123.0484593], [40.7062544, -123.0485218], [40.7053854, -123.0483732], [40.7046453, -123.0480554], [40.7041867, -123.0477168], [40.7041676, -123.0476784], [40.7039877, -123.0473159], [40.7039294, -123.0471984], [40.7036157, -123.0468916], [40.700744, -123.0444261], [40.7001246, -123.0437595], [40.6998995, -123.0431355], [40.6995378, -123.0422367], [40.6987578, -123.0403965], [40.6987271, -123.0402776], [40.6987201, -123.0402505], [40.6984846, -123.0393391], [40.6980906, -123.038842], [40.6974794, -123.0375412], [40.6972785, -123.0368327], [40.6970774, -123.0363356], [40.6969005, -123.0361347], [40.6965787, -123.0359019], [40.6961765, -123.0354788], [40.6959191, -123.0350928], [40.6956859, -123.034638], [40.6951955, -123.0329358], [40.6950589, -123.0322908], [40.6948901, -123.0315189], [40.6949064, -123.0310432], [40.694826, -123.0307154], [40.6947215, -123.0299859], [40.6947539, -123.0295525], [40.6947381, -123.0279878], [40.6945774, -123.0274169], [40.6943521, -123.0270996], [40.6940625, -123.0265709], [40.6939916, -123.0265066], [40.6937246, -123.0262642], [40.6936014, -123.0262683], [40.6934108, -123.0262746], [40.6930245, -123.0262744], [40.6926706, -123.0259466], [40.6921798, -123.0256186], [40.6917694, -123.0254916], [40.6914234, -123.0254703], [40.6911579, -123.0255443], [40.6906348, -123.025988], [40.6903047, -123.0264213], [40.6899344, -123.026918], [40.6890893, -123.0280277], [40.688558, -123.028482], [40.6883247, -123.0285665], [40.6881638, -123.028577], [40.6879304, -123.0285029], [40.6876649, -123.0283072], [40.6872224, -123.0280639], [40.6863775, -123.0278098], [40.6857258, -123.0275982], [40.6852913, -123.0275134], [40.6845671, -123.0272383], [40.6840361, -123.0269632], [40.6837142, -123.0269208], [40.6833039, -123.0269841], [40.6827808, -123.0271424], [40.6823496, -123.0274465], [40.6822415, -123.0275227], [40.6809379, -123.027649], [40.680447, -123.0277229], [40.6796181, -123.0280078], [40.6786847, -123.0281555], [40.6782984, -123.0282715], [40.677558, -123.0283663], [40.6772121, -123.0284719], [40.677043, -123.0285881], [40.6765118, -123.0290741], [40.676375, -123.0291902], [40.6755461, -123.0293907], [40.6752242, -123.0294117], [40.6748058, -123.0293376], [40.6745507, -123.0293375], [40.6737517, -123.0293371], [40.6730516, -123.0295164], [40.6725768, -123.0293788], [40.672247, -123.0291567], [40.6718849, -123.0287762], [40.6713621, -123.0280573], [40.6709277, -123.0276132], [40.6706541, -123.027444], [40.6691781, -123.0238106], [40.6690697, -123.0235438], [40.6683056, -123.0218526], [40.6682503, -123.0217085], [40.6677667, -123.0204469], [40.6675737, -123.0199713], [40.6675979, -123.0196331], [40.6676141, -123.0192844], [40.6675256, -123.0187877], [40.6673004, -123.0178418], [40.6671557, -123.0172711], [40.6670028, -123.0168907], [40.6667937, -123.0166053], [40.6665764, -123.0164784], [40.6662867, -123.016362], [40.6656913, -123.0164782], [40.6653855, -123.016531], [40.6649268, -123.0163407], [40.6646935, -123.0163194], [40.6643072, -123.0163299], [40.6638796, -123.0162042], [40.6634865, -123.015981], [40.6632291, -123.0155265], [40.6631889, -123.0151038], [40.6632935, -123.0147975], [40.6637442, -123.0139944], [40.6642674, -123.0131492], [40.664702, -123.0126843], [40.6651688, -123.0118707], [40.6656195, -123.0108668], [40.6659581, -123.0101871], [40.6661829, -123.0097362], [40.6663117, -123.0092079], [40.6663761, -123.0086161], [40.6664486, -123.0082991], [40.6664969, -123.0080243], [40.6664646, -123.0076967], [40.6664084, -123.0069992], [40.6664004, -123.0063546], [40.666167, -123.0056465], [40.6660706, -123.0049069], [40.6664005, -123.0034591], [40.6668672, -123.0025186], [40.6674467, -123.0016838], [40.6677104, -123.0011379], [40.6679424, -123.0004282]], [[40.7605914, -123.1128517], [40.7604967, -123.112989], [40.760384, -123.1130958], [40.7601991, -123.1133016], [40.7600458, -123.1135003], [40.7599149, -123.1136832], [40.7596624, -123.114019], [40.759518, -123.114225], [40.759324, -123.1145456], [40.7592158, -123.1146524], [40.7591391, -123.1147593], [40.7590219, -123.1148505], [40.7589318, -123.1149422], [40.7588686, -123.1150184], [40.7586613, -123.1151787], [40.7584539, -123.1153694], [40.7582826, -123.1154686], [40.7581429, -123.1155602]], [[40.7764634, -123.1387623], [40.7763557, -123.1384799], [40.7762344, -123.1382204], [40.7761805, -123.1380526], [40.7761672, -123.1378847]], [[40.7816429, -123.0999356]], [[40.7872337, -123.1265399], [40.7872245, -123.1267154]], [[40.7871388, -123.1268605]], [[40.765416, -123.144589], [40.7653801, -123.1445649]], [[40.7648306, -123.1444915]], [[40.7646505, -123.144443]], [[40.7642948, -123.1443704]], [[40.7641912, -123.1443461]], [[40.7640111, -123.1442734]], [[40.7639167, -123.1442129], [40.7638806, -123.144201]], [[40.7637275, -123.1440925]], [[40.7688134, -123.1401963]], [[40.7885685, -123.1208865], [40.7886088, -123.1211229], [40.7886356, -123.121344], [40.788622, -123.1214967], [40.7886172, -123.1217103]], [[40.7901501, -123.1365652], [40.7899344, -123.1361454], [40.7896334, -123.1354666], [40.7895661, -123.1352072], [40.7894538, -123.1349403], [40.7893234, -123.134757], [40.789202, -123.1346046], [40.789049, -123.1344746], [40.7889725, -123.1344366], [40.7887744, -123.1343222], [40.7885312, -123.1342762], [40.7884232, -123.1342459], [40.7882384, -123.134284], [40.7881709, -123.1342917]], [[40.7814503, -123.1179258]], [[40.7872736, -123.1142564], [40.7872918, -123.1140349], [40.787301, -123.113875]], [[40.7872566, -123.1131956]], [[40.7773141, -123.1499307]], [[40.7772336, -123.1494735]], [[40.7771307, -123.1490041]], [[40.7770678, -123.1488235]], [[40.7770409, -123.1487272]], [[40.7767761, -123.1480052]], [[40.7767311, -123.1479089]], [[40.7766595, -123.1476202]], [[40.7765392, -123.1466097]], [[40.7766171, -123.1455033]], [[40.7766264, -123.1453111]], [[40.7766445, -123.1452149]]]

woodlandPath = '/Users/Marko/Downloads/WOODLAND_6_California_GU_STATEORTERRITORY/WOODLAND_6_California_GU_STATEORTERRITORY.gdb'
aquaticPath = '/Users/Marko/Downloads/NHD_H_California_State_GDB/NHD_H_California_State_GDB.gdb'

if '--weaverville' in sys.argv:
	if '--keepTerrain' in sys.argv: baseImage = Image.open('Weaverville Terrain Thumbnail.png')
	else: baseImage = Image.open('Weaverville Blackdrop.png')
	minX = -124
	maxX = -122
	minY = 40
	maxY = 42

else:
	baseImage = Image.open('blackcali.png')
	minX = -125
	maxX = -114
	minY = 32
	maxY = 43

if '--aqua' in sys.argv or '--cyan' in sys.argv: fillColor = (0,255,255)
elif '--green' in sys.argv: fillColor = (0,255,0)
elif '--red' in sys.argv: fillColor = (255,0,0)
elif '--blue' in sys.argv: fillColor = (0,0,255)
else: fillColor = (255,255,255)

if '--lakes' in sys.argv:
	dataIndex = 27
	databasePath = aquaticPath
elif '--creeks' in sys.argv:
	dataIndex = 22
	databasePath = aquaticPath
elif '--rivers' in sys.argv:
	dataIndex = 24
	databasePath = aquaticPath
else:
	dataIndex = 3
	databasePath = woodlandPath
	
outputName = 'Output.png'
for term in sys.argv:
	if '.png' in term: outputName = term


baseWidth, baseHeight = baseImage.size
draw = ImageDraw.Draw(baseImage)

driver = ogr.GetDriverByName("OpenFileGDB")
dataset = driver.Open(databasePath, 0)

validPolys = 0

minXfound = None
maxXfound = None
minYfound = None
maxYfound = None

maxIter = len(dataset[3])
if '--custom' in sys.argv: maxIter = len(customPoly)
for i in range(1,maxIter):
	
	try:
		if '--custom' in sys.argv:
			poly = []
			for coordinate in customPoly[i]: poly.append([coordinate[1],coordinate[0]])
		else:
			if dataIndex == 22: poly = json.loads(dataset[dataIndex][i].ExportToJson())['geometry']['coordinates'][0]
			else: poly = json.loads(dataset[dataIndex][i].ExportToJson())['geometry']['coordinates'][0][0]
	except:
		continue
	
#	for coord in poly:
#		if minXfound == None or coord[0] < minXfound:
#			minXfound = coord[0]
##			print('MinX:'+str(minXfound)+' MaxX:'+str(maxXfound)+' MinY:'+str(minYfound)+' MaxY:'+str(maxYfound)+' '+str(i),'/',str(len(dataset[3])))
#		if maxXfound == None or coord[0] > maxXfound:
#			maxXfound = coord[0]
##			print('MinX:'+str(minXfound)+' MaxX:'+str(maxXfound)+' MinY:'+str(minYfound)+' MaxY:'+str(maxYfound)+' '+str(i),'/',str(len(dataset[3])))
#		if minYfound == None or coord[1] < minYfound:
#			minYfound = coord[1]
##			print('MinX:'+str(minXfound)+' MaxX:'+str(maxXfound)+' MinY:'+str(minYfound)+' MaxY:'+str(maxYfound)+' '+str(i),'/',str(len(dataset[3])))
#		if maxYfound == None or coord[1] > maxYfound:
#			maxYfound = coord[1]
##			print('MinX:'+str(minXfound)+' MaxX:'+str(maxXfound)+' MinY:'+str(minYfound)+' MaxY:'+str(maxYfound)+' '+str(i),'/',str(len(dataset[3])))
		

	
	polyInBounds = False
	for coord in poly:
		if coord[0] > minX and coord[0] < maxX and coord[1] > minY and coord[1] < maxY:
			polyInBounds = True
			
	if polyInBounds:
		fixedPoly = []
		for coord in poly:
			xCoor = int((coord[0]-minX)*baseWidth/(maxX-minX))
			yCoor = baseHeight-int((coord[1]-minY)*baseHeight/(maxY-minY))
			if xCoor < 0: xCoor = 0
			if xCoor > baseWidth: xCoor = baseWidth
			if yCoor < 0: yCoor = 0
			if yCoor > baseHeight: yCoor = baseHeight
			fixedPoly.append((xCoor,yCoor))
			
#		print(poly[0],fixedPoly[0])
#		if i >= 1: print(fixedPoly)
			
		# Draw the poly
		if dataIndex != 22 and not ('--custom' in sys.argv): draw.polygon(fixedPoly, fill=fillColor)
		else: draw.line(fixedPoly, fill=fillColor, width=5)
		validPolys += 1
	
	if i%int(len(dataset[dataIndex])/1000)==0:
		perc = str(i/len(dataset[dataIndex])*100)
		if perc[1] == '.': print(perc[:3]+'%')
		else: print(perc[:4]+'%')
	if i%10000 == 0:
		baseImage.save('WeaverCreeks_'+str(i)+'.png')
		baseImage.show()
		
baseImage.show()
baseImage.save(outputName)
			
			