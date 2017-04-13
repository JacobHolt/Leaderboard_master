import random
import csv

last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham", "Sullivan", "Wallace", "Woods", "Cole", "West", "Jordan", "Owens", "Reynolds", "Fisher", "Ellis", "Harrison", "Gibson", "McDonald", "Cruz", "Marshall", "Ortiz", "Gomez", "Murray", "Freeman", "Wells", "Webb", "Simpson", "Stevens", "Tucker", "Porter", "Hunter", "Hicks", "Crawford", "Henry", "Boyd", "Mason", "Morales", "Kennedy", "Warren", "Dixon", "Ramos", "Reyes", "Burns", "Gordon", "Shaw", "Holmes", "Rice", "Robertson", "Hunt", "Black", "Daniels", "Palmer", "Mills", "Nichols", "Grant", "Knight", "Ferguson", "Rose", "Stone", "Hawkins", "Dunn", "Perkins", "Hudson", "Spencer", "Gardner", "Stephens", "Payne", "Pierce", "Berry", "Matthews", "Arnold", "Wagner", "Willis", "Ray", "Watkins", "Olson", "Carroll", "Duncan", "Snyder", "Hart", "Cunningham", "Bradley", "Lane", "Andrews", "Ruiz", "Harper", "Fox", "Riley", "Armstrong", "Carpenter", "Weaver", "Greene", "Lawrence", "Elliott", "Chavez", "Sims", "Austin", "Peters", "Kelley", "Franklin", "Lawson", "Fields", "Gutierrez", "Ryan", "Schmidt", "Carr", "Vasquez", "Castillo", "Wheeler", "Chapman", "Oliver", "Montgomery", "Richards", "Williamson", "Johnston", "Banks", "Meyer", "Bishop", "McCoy", "Howell", "Alvarez", "Morrison", "Hansen", "Fernandez", "Garza", "Harvey", "Little", "Burton", "Stanley", "Nguyen", "George", "Jacobs", "Reid", "Kim", "Fuller", "Lynch", "Dean", "Gilbert", "Garrett", "Romero", "Welch", "Larson", "Frazier", "Burke", "Hanson", "Day", "Mendoza", "Moreno", "Bowman", "Medina", "Fowler", "Brewer", "Hoffman", "Carlson", "Silva", "Pearson", "Holland", "Douglas", "Fleming", "Jensen", "Vargas", "Byrd", "Davidson", "Hopkins", "May", "Terry", "Herrera", "Wade", "Soto", "Walters", "Curtis", "Neal", "Caldwell", "Lowe", "Jennings", "Barnett", "Graves", "Jimenez", "Horton", "Shelton", "Barrett", "O'Brien", "Castro", "Sutton", "Gregory", "McKinney", "Lucas", "Miles", "Craig", "Rodriquez", "Chambers", "Holt", "Lambert", "Fletcher", "Watts", "Bates", "Hale", "Rhodes", "Pena", "Beck", "Newman", "Haynes", "McDaniel", "Mendez", "Bush", "Vaughn", "Parks", "Dawson", "Santiago", "Norris", "Hardy", "Love", "Steele", "Curry", "Powers", "Schultz", "Barker", "Guzman", "Page", "Munoz", "Ball", "Keller", "Chandler", "Weber", "Leonard", "Walsh", "Lyons", "Ramsey", "Wolfe", "Schneider", "Mullins", "Benson", "Sharp", "Bowen", "Daniel", "Barber", "Cummings", "Hines", "Baldwin", "Griffith", "Valdez", "Hubbard", "Salazar", "Reeves", "Warner", "Stevenson", "Burgess", "Santos", "Tate", "Cross", "Garner", "Mann", "Mack", "Moss", "Thornton", "Dennis", "McGee", "Farmer", "Delgado", "Aguilar", "Vega", "Glover", "Manning", "Cohen", "Harmon", "Rodgers", "Robbins", "Newton", "Todd", "Blair", "Higgins", "Ingram", "Reese", "Cannon", "Strickland", "Townsend", "Potter", "Goodwin", "Walton", "Rowe", "Hampton", "Ortega", "Patton", "Swanson", "Joseph", "Francis", "Goodman", "Maldonado", "Yates", "Becker", "Erickson", "Hodges", "Rios", "Conner", "Adkins", "Webster", "Norman", "Malone", "Hammond", "Flowers", "Cobb", "Moody", "Quinn", "Blake", "Maxwell", "Pope", "Floyd", "Osborne", "Paul", "McCarthy", "Guerrero", "Lindsey", "Estrada", "Sandoval", "Gibbs", "Tyler", "Gross", "Fitzgerald", "Stokes", "Doyle", "Sherman", "Saunders", "Wise", "Colon", "Gill", "Alvarado", "Greer", "Padilla", "Simon", "Waters", "Nunez", "Ballard", "Schwartz", "McBride", "Houston", "Christensen", "Klein", "Pratt", "Briggs", "Parsons", "McLaughlin", "Zimmerman", "French", "Buchanan", "Moran", "Copeland", "Roy", "Pittman", "Brady", "McCormick", "Holloway", "Brock", "Poole", "Frank", "Logan", "Owen", "Bass", "Marsh", "Drake", "Wong", "Jefferson", "Park", "Morton", "Abbott", "Sparks", "Patrick", "Norton", "Huff", "Clayton", "Massey", "Lloyd", "Figueroa", "Carson", "Bowers", "Roberson", "Barton", "Tran", "Lamb", "Harrington", "Casey", "Boone", "Cortez", "Clarke", "Mathis", "Singleton", "Wilkins", "Cain", "Bryan", "Underwood", "Hogan", "McKenzie", "Collier", "Luna", "Phelps", "McGuire", "Allison", "Bridges", "Wilkerson", "Nash", "Summers", "Atkins", "Wilcox", "Pitts", "Conley", "Marquez", "Burnett", "Richard", "Cochran", "Chase", "Davenport", "Hood", "Gates", "Clay", "Ayala", "Sawyer", "Roman", "Vazquez", "Dickerson", "Hodge", "Acosta", "Flynn", "Espinoza", "Nicholson", "Monroe", "Wolf", "Morrow", "Kirk", "Randall", "Anthony", "Whitaker", "O'Connor", "Skinner", "Ware", "Molina", "Kirby", "Huffman", "Bradford", "Charles", "Gilmore", "Dominguez", "O'Neal", "Bruce", "Lang", "Combs", "Kramer", "Heath", "Hancock", "Gallagher", "Gaines", "Shaffer", "Short", "Wiggins", "Mathews", "McClain", "Fischer", "Wall", "Small", "Melton", "Hensley", "Bond", "Dyer", "Cameron", "Grimes", "Contreras", "Christian", "Wyatt", "Baxter", "Snow", "Mosley", "Shepherd", "Larsen", "Hoover", "Beasley", "Glenn", "Petersen", "Whitehead", "Meyers", "Keith", "Garrison", "Vincent", "Shields", "Horn", "Savage", "Olsen", "Schroeder", "Hartman", "Woodard", "Mueller", "Kemp", "Deleon", "Booth", "Patel", "Calhoun", "Wiley", "Eaton", "Cline", "Navarro", "Harrell", "Lester", "Humphrey", "Parrish", "Duran", "Hutchinson", "Hess", "Dorsey", "Bullock", "Robles", "Beard", "Dalton", "Avila", "Vance", "Rich", "Blackwell", "York", "Johns", "Blankenship", "Trevino", "Salinas", "Campos", "Pruitt", "Moses", "Callahan", "Golden", "Montoya", "Hardin", "Guerra", "McDowell", "Carey", "Stafford", "Gallegos", "Henson", "Wilkinson", "Booker", "Merritt", "Miranda", "Atkinson", "Orr", "Decker", "Hobbs", "Preston", "Tanner", "Knox", "Pacheco", "Stephenson", "Glass", "Rojas", "Serrano", "Marks", "Hickman", "English", "Sweeney", "Strong", "Prince", "McClure", "Conway", "Walter", "Roth", "Maynard", "Farrell", "Lowery", "Hurst", "Nixon", "Weiss", "Trujillo", "Ellison", "Sloan", "Juarez", "Winters", "McLean", "Randolph", "Leon", "Boyer", "Villarreal", "McCall", "Gentry", "Carrillo", "Kent", "Ayers", "Lara", "Shannon", "Sexton", "Pace", "Hull", "Leblanc", "Browning", "Velasquez", "Leach", "Chang", "House", "Sellers", "Herring", "Noble", "Foley", "Bartlett", "Mercado", "Landry", "Durham", "Walls", "Barr", "McKee", "Bauer", "Rivers", "Everett", "Bradshaw", "Pugh", "Velez", "Rush", "Estes", "Dodson", "Morse", "Sheppard", "Weeks", "Camacho", "Bean", "Barron", "Livingston", "Middleton", "Spears", "Branch", "Blevins", "Chen", "Kerr", "McConnell", "Hatfield", "Harding", "Ashley", "Solis", "Herman", "Frost", "Giles", "Blackburn", "William", "Pennington", "Woodward", "Finley", "McIntosh", "Koch", "Best", "Solomon", "McCullough", "Dudley", "Nolan", "Blanchard", "Rivas", "Brennan", "Mejia", "Kane", "Benton", "Joyce", "Buckley", "Haley", "Valentine", "Maddox", "Russo", "McKnight", "Buck", "Moon", "McMillan", "Crosby", "Berg", "Dotson", "Mays", "Roach", "Church", "Chan", "Richmond", "Meadows", "Faulkner", "O'Neill", "Knapp", "Kline", "Barry", "Ochoa", "Jacobson", "Gay", "Avery", "Hendricks", "Horne", "Shepard", "Hebert", "Cherry", "Cardenas", "McIntyre", "Whitney", "Waller", "Holman", "Donaldson", "Cantu", "Terrell", "Morin", "Gillespie", "Fuentes", "Tillman", "Sanford", "Bentley", "Peck", "Key", "Salas", "Rollins", "Gamble", "Dickson", "Battle", "Santana", "Cabrera", "Cervantes", "Howe", "Hinton", "Hurley", "Spence", "Zamora", "Yang", "McNeil", "Suarez", "Case", "Petty", "Gould", "McFarland", "Sampson", "Carver", "Bray", "Rosario", "MacDonald", "Stout", "Hester", "Melendez", "Dillon", "Farley", "Hopper", "Galloway", "Potts", "Bernard", "Joyner", "Stein", "Aguirre", "Osborn", "Mercer", "Bender", "Franco", "Rowland", "Sykes", "Benjamin", "Travis", "Pickett", "Crane", "Sears", "Mayo", "Dunlap", "Hayden", "Wilder", "McKay", "Coffey", "McCarty", "Ewing", "Cooley", "Vaughan", "Bonner", "Cotton", "Holder", "Stark", "Ferrell", "Cantrell", "Fulton", "Lynn", "Lott", "Calderon", "Rosa", "Pollard", "Hooper", "Burch", "Mullen", "Fry", "Riddle", "Levy", "David", "Duke", "O'Donnell", "Guy", "Michael", "Britt", "Frederick", "Daugherty", "Berger", "Dillard", "Alston", "Jarvis", "Frye", "Riggs", "Chaney", "Odom", "Duffy", "Fitzpatrick", "Valenzuela", "Merrill", "Mayer", "Alford", "McPherson", "Acevedo", "Donovan", "Barrera", "Albert", "Cote", "Reilly", "Compton", "Raymond", "Mooney", "McGowan", "Craft", "Cleveland", "Clemons", "Wynn", "Nielsen", "Baird", "Stanton", "Snider", "Rosales", "Bright", "Witt", "Stuart", "Hays", "Holden", "Rutledge", "Kinney", "Clements", "Castaneda", "Slater", "Hahn", "Emerson", "Conrad", "Burks", "Delaney", "Pate", "Lancaster", "Sweet", "Justice", "Tyson", "Sharpe", "Whitfield", "Talley", "Macias", "Irwin", "Burris", "Ratliff", "McCray", "Madden", "Kaufman", "Beach", "Goff", "Cash", "Bolton", "McFadden", "Levine", "Good", "Byers", "Kirkland", "Kidd", "Workman", "Carney", "Dale", "McLeod", "Holcomb", "England", "Finch", "Head", "Burt", "Hendrix", "Sosa", "Haney", "Franks", "Sargent", "Nieves", "Downs", "Rasmussen", "Bird", "Hewitt", "Lindsay", "Le", "Foreman", "Valencia", "O'Neil", "Delacruz", "Vinson", "Dejesus", "Hyde", "Forbes", "Gilliam", "Guthrie", "Wooten", "Huber", "Barlow", "Boyle", "McMahon", "Buckner", "Rocha", "Puckett", "Langley", "Knowles", "Cooke", "Velazquez", "Whitley", "Noel", "Vang"]
first_female = ["MARY", "PATRICIA", "LINDA", "BARBARA", "ELIZABETH", "JENNIFER", "MARIA", "SUSAN", "MARGARET", "DOROTHY", "LISA", "NANCY", "KAREN", "BETTY", "HELEN", "SANDRA", "DONNA", "CAROL", "RUTH", "SHARON", "MICHELLE", "LAURA", "SARAH", "KIMBERLY", "DEBORAH", "JESSICA", "SHIRLEY", "CYNTHIA", "ANGELA", "MELISSA", "BRENDA", "AMY", "ANNA", "REBECCA", "VIRGINIA", "KATHLEEN", "PAMELA", "MARTHA", "DEBRA", "AMANDA", "STEPHANIE", "CAROLYN", "CHRISTINE", "MARIE", "JANET", "CATHERINE", "FRANCES", "ANN", "JOYCE", "DIANE", "ALICE", "JULIE", "HEATHER", "TERESA", "DORIS", "GLORIA", "EVELYN", "JEAN", "CHERYL", "MILDRED", "KATHERINE", "JOAN", "ASHLEY", "JUDITH", "ROSE", "JANICE", "KELLY", "NICOLE", "JUDY", "CHRISTINA", "KATHY", "THERESA", "BEVERLY", "DENISE", "TAMMY", "IRENE", "JANE", "LORI", "RACHEL", "MARILYN", "ANDREA", "KATHRYN", "LOUISE", "SARA", "ANNE", "JACQUELINE", "WANDA", "BONNIE", "JULIA", "RUBY", "LOIS", "TINA", "PHYLLIS", "NORMA", "PAULA", "DIANA", "ANNIE", "LILLIAN", "EMILY", "ROBIN", "PEGGY", "CRYSTAL", "GLADYS", "RITA", "DAWN", "CONNIE", "FLORENCE", "TRACY", "EDNA", "TIFFANY", "CARMEN", "ROSA", "CINDY", "GRACE", "WENDY", "VICTORIA", "EDITH", "KIM", "SHERRY", "SYLVIA", "JOSEPHINE", "THELMA", "SHANNON", "SHEILA", "ETHEL", "ELLEN", "ELAINE", "MARJORIE", "CARRIE", "CHARLOTTE", "MONICA", "ESTHER", "PAULINE", "EMMA", "JUANITA", "ANITA", "RHONDA", "HAZEL", "AMBER", "EVA", "DEBBIE", "APRIL", "LESLIE", "CLARA", "LUCILLE", "JAMIE", "JOANNE", "ELEANOR", "VALERIE", "DANIELLE", "MEGAN", "ALICIA", "SUZANNE", "MICHELE", "GAIL", "BERTHA", "DARLENE", "VERONICA", "JILL", "ERIN", "GERALDINE", "LAUREN", "CATHY", "JOANN", "LORRAINE", "LYNN", "SALLY", "REGINA", "ERICA", "BEATRICE", "DOLORES", "BERNICE", "AUDREY", "YVONNE", "ANNETTE", "JUNE", "SAMANTHA", "MARION", "DANA", "STACY", "ANA", "RENEE", "IDA", "VIVIAN", "ROBERTA", "HOLLY", "BRITTANY", "MELANIE", "LORETTA", "YOLANDA", "JEANETTE", "LAURIE", "KATIE", "KRISTEN", "VANESSA", "ALMA", "SUE", "ELSIE", "BETH", "JEANNE", "VICKI", "CARLA", "TARA", "ROSEMARY", "EILEEN", "TERRI", "GERTRUDE", "LUCY", "TONYA", "ELLA", "STACEY", "WILMA", "GINA", "KRISTIN", "JESSIE", "NATALIE", "AGNES", "VERA", "WILLIE", "CHARLENE", "BESSIE", "DELORES", "MELINDA", "PEARL", "ARLENE", "MAUREEN", "COLLEEN", "ALLISON", "TAMARA", "JOY", "GEORGIA", "CONSTANCE", "LILLIE", "CLAUDIA", "JACKIE", "MARCIA", "TANYA", "NELLIE", "MINNIE", "MARLENE", "HEIDI", "GLENDA", "LYDIA", "VIOLA", "COURTNEY", "MARIAN", "STELLA", "CAROLINE", "DORA", "JO", "VICKIE", "MATTIE", "TERRY", "MAXINE", "IRMA", "MABEL", "MARSHA", "MYRTLE", "LENA", "CHRISTY", "DEANNA", "PATSY", "HILDA", "GWENDOLYN", "JENNIE", "NORA", "MARGIE", "NINA", "CASSANDRA", "LEAH", "PENNY", "KAY", "PRISCILLA", "NAOMI", "CAROLE", "BRANDY", "OLGA", "BILLIE", "DIANNE", "TRACEY", "LEONA", "JENNY", "FELICIA", "SONIA", "MIRIAM", "VELMA", "BECKY", "BOBBIE", "VIOLET", "KRISTINA", "TONI", "MISTY", "MAE", "SHELLY", "DAISY", "RAMONA", "SHERRI", "ERIKA", "KATRINA", "CLAIRE", "LINDSEY", "LINDSAY", "GENEVA", "GUADALUPE", "BELINDA", "MARGARITA", "SHERYL", "CORA", "FAYE", "ADA", "NATASHA", "SABRINA", "ISABEL", "MARGUERITE", "HATTIE", "HARRIET", "MOLLY", "CECILIA", "KRISTI", "BRANDI", "BLANCHE", "SANDY", "ROSIE", "JOANNA", "IRIS", "EUNICE", "ANGIE", "INEZ", "LYNDA", "MADELINE", "AMELIA", "ALBERTA", "GENEVIEVE", "MONIQUE", "JODI", "JANIE", "MAGGIE", "KAYLA", "SONYA", "JAN", "LEE", "KRISTINE", "CANDACE", "FANNIE", "MARYANN", "OPAL", "ALISON", "YVETTE", "MELODY", "LUZ", "SUSIE", "OLIVIA", "FLORA", "SHELLEY", "KRISTY", "MAMIE", "LULA", "LOLA", "VERNA", "BEULAH", "ANTOINETTE", "CANDICE", "JUANA", "JEANNETTE", "PAM", "KELLI", "HANNAH", "WHITNEY", "BRIDGET", "KARLA", "CELIA", "LATOYA", "PATTY", "SHELIA", "GAYLE", "DELLA", "VICKY", "LYNNE", "SHERI", "MARIANNE", "KARA", "JACQUELYN", "ERMA", "BLANCA", "MYRA", "LETICIA", "PAT", "KRISTA", "ROXANNE", "ANGELICA", "JOHNNIE", "ROBYN", "FRANCIS", "ADRIENNE", "ROSALIE", "ALEXANDRA", "BROOKE", "BETHANY", "SADIE", "BERNADETTE", "TRACI", "JODY", "KENDRA", "JASMINE", "NICHOLE", "RACHAEL", "CHELSEA", "MABLE", "ERNESTINE", "MURIEL", "MARCELLA", "ELENA", "KRYSTAL", "ANGELINA", "NADINE", "KARI", "ESTELLE", "DIANNA", "PAULETTE", "LORA", "MONA", "DOREEN", "ROSEMARIE", "ANGEL", "DESIREE", "ANTONIA", "HOPE", "GINGER", "JANIS", "BETSY", "CHRISTIE", "FREDA", "MERCEDES", "MEREDITH", "LYNETTE", "TERI", "CRISTINA", "EULA", "LEIGH", "MEGHAN", "SOPHIA", "ELOISE", "ROCHELLE", "GRETCHEN", "CECELIA", "RAQUEL", "HENRIETTA", "ALYSSA", "JANA", "KELLEY", "GWEN", "KERRY", "JENNA", "TRICIA", "LAVERNE", "OLIVE", "ALEXIS", "TASHA", "SILVIA", "ELVIRA", "CASEY", "DELIA", "SOPHIE", "KATE", "PATTI", "LORENA", "KELLIE", "SONJA", "LILA", "LANA", "DARLA", "MAY", "MINDY", "ESSIE", "MANDY", "LORENE", "ELSA", "JOSEFINA", "JEANNIE", "MIRANDA", "DIXIE", "LUCIA", "MARTA", "FAITH", "LELA", "JOHANNA", "SHARI", "CAMILLE", "TAMI", "SHAWNA", "ELISA", "EBONY", "MELBA", "ORA", "NETTIE", "TABITHA", "OLLIE", "JAIME", "WINIFRED", "KRISTIE", "MARINA", "ALISHA", "AIMEE", "RENA", "MYRNA", "MARLA", "TAMMIE", "LATASHA", "BONITA", "PATRICE", "RONDA", "SHERRIE", "ADDIE", "FRANCINE", "DELORIS", "STACIE", "ADRIANA", "CHERI", "SHELBY", "ABIGAIL", "CELESTE", "JEWEL", "CARA", "ADELE", "REBEKAH", "LUCINDA", "DORTHY", "CHRIS", "EFFIE", "TRINA", "REBA", "SHAWN", "SALLIE", "AURORA", "LENORA", "ETTA", "LOTTIE", "KERRI", "TRISHA", "NIKKI", "ESTELLA", "FRANCISCA", "JOSIE", "TRACIE", "MARISSA", "KARIN", "BRITTNEY", "JANELLE", "LOURDES", "LAUREL", "HELENE", "FERN", "ELVA", "CORINNE", "KELSEY", "INA", "BETTIE", "ELISABETH", "AIDA", "CAITLIN", "INGRID", "IVA", "EUGENIA", "CHRISTA", "GOLDIE", "CASSIE", "MAUDE", "JENIFER", "THERESE", "FRANKIE", "DENA", "LORNA", "JANETTE", "LATONYA", "CANDY", "MORGAN", "CONSUELO", "TAMIKA", "ROSETTA", "DEBORA", "CHERIE", "POLLY", "DINA", "JEWELL", "FAY", "JILLIAN", "DOROTHEA", "NELL", "TRUDY", "ESPERANZA", "PATRICA", "KIMBERLEY", "SHANNA", "HELENA", "CAROLINA", "CLEO", "STEFANIE", "ROSARIO", "OLA", "JANINE", "MOLLIE", "LUPE", "ALISA", "LOU", "MARIBEL", "SUSANNE", "BETTE", "SUSANA", "ELISE", "CECILE", "ISABELLE", "LESLEY", "JOCELYN", "PAIGE", "JONI", "RACHELLE", "LEOLA", "DAPHNE", "ALTA", "ESTER", "PETRA", "GRACIELA", "IMOGENE", "JOLENE", "KEISHA", "LACEY", "GLENNA", "GABRIELA", "KERI", "URSULA", "LIZZIE", "KIRSTEN", "SHANA", "ADELINE", "MAYRA", "JAYNE", "JACLYN", "GRACIE", "SONDRA", "CARMELA", "MARISA", "ROSALIND", "CHARITY", "TONIA", "BEATRIZ", "MARISOL", "CLARICE", "JEANINE", "SHEENA", "ANGELINE", "FRIEDA", "LILY", "ROBBIE", "SHAUNA", "MILLIE", "CLAUDETTE", "CATHLEEN", "ANGELIA", "GABRIELLE", "AUTUMN", "KATHARINE", "SUMMER", "JODIE", "STACI", "LEA", "CHRISTI", "JIMMIE", "JUSTINE", "ELMA", "LUELLA", "MARGRET", "DOMINIQUE", "SOCORRO", "RENE", "MARTINA", "MARGO", "MAVIS", "CALLIE", "BOBBI", "MARITZA", "LUCILE", "LEANNE", "JEANNINE", "DEANA", "AILEEN", "LORIE", "LADONNA", "WILLA", "MANUELA", "GALE", "SELMA", "DOLLY", "SYBIL", "ABBY", "LARA", "DALE", "IVY", "DEE", "WINNIE", "MARCY", "LUISA", "JERI", "MAGDALENA", "OFELIA", "MEAGAN", "AUDRA", "MATILDA", "LEILA", "CORNELIA", "BIANCA", "SIMONE", "BETTYE", "RANDI", "VIRGIE", "LATISHA", "BARBRA", "GEORGINA", "ELIZA", "LEANN", "BRIDGETTE", "RHODA", "HALEY", "ADELA", "NOLA", "BERNADINE", "FLOSSIE", "ILA", "GRETA", "RUTHIE", "NELDA", "MINERVA", "LILLY", "TERRIE", "LETHA", "HILARY", "ESTELA", "VALARIE", "BRIANNA", "ROSALYN", "EARLINE", "CATALINA", "AVA", "MIA", "CLARISSA", "LIDIA", "CORRINE", "ALEXANDRIA", "CONCEPCION", "TIA", "SHARRON", "RAE", "DONA", "ERICKA", "JAMI", "ELNORA", "CHANDRA", "LENORE", "NEVA", "MARYLOU", "MELISA", "TABATHA", "SERENA", "AVIS", "ALLIE", "SOFIA", "JEANIE", "ODESSA", "NANNIE", "HARRIETT", "LORAINE", "PENELOPE", "MILAGROS", "EMILIA", "BENITA", "ALLYSON", "ASHLEE", "TANIA", "TOMMIE", "ESMERALDA", "KARINA", "EVE", "PEARLIE", "ZELMA", "MALINDA", "NOREEN", "TAMEKA", "SAUNDRA", "HILLARY", "AMIE", "ALTHEA", "ROSALINDA", "JORDAN", "LILIA", "ALANA", "GAY", "CLARE", "ALEJANDRA", "ELINOR", "MICHAEL", "LORRIE", "JERRI", "DARCY", "EARNESTINE", "CARMELLA", "TAYLOR", "NOEMI", "MARCIE", "LIZA", "ANNABELLE", "LOUISA", "EARLENE", "MALLORY", "CARLENE", "NITA", "SELENA", "TANISHA", "KATY", "JULIANNE", "JOHN", "LAKISHA", "EDWINA", "MARICELA", "MARGERY", "KENYA", "DOLLIE", "ROXIE", "ROSLYN", "KATHRINE", "NANETTE", "CHARMAINE", "LAVONNE", "ILENE", "KRIS", "TAMMI", "SUZETTE", "CORINE", "KAYE", "JERRY", "MERLE", "CHRYSTAL", "LINA", "DEANNE", "LILIAN", "JULIANA", "ALINE", "LUANN", "KASEY", "MARYANNE", "EVANGELINE", "COLETTE", "MELVA", "LAWANDA", "YESENIA", "NADIA", "MADGE", "KATHIE", "EDDIE", "OPHELIA", "VALERIA", "NONA", "MITZI", "MARI", "GEORGETTE", "CLAUDINE", "FRAN", "ALISSA", "ROSEANN", "LAKEISHA", "SUSANNA", "REVA", "DEIDRE", "CHASITY", "SHEREE", "CARLY", "JAMES", "ELVIA", "ALYCE", "DEIRDRE", "GENA", "BRIANA", "ARACELI", "KATELYN", "ROSANNE", "WENDI", "TESSA", "BERTA", "MARVA", "IMELDA", "MARIETTA", "MARCI", "LEONOR", "ARLINE", "SASHA", "MADELYN", "JANNA", "JULIETTE", "DEENA", "AURELIA", "JOSEFA", "AUGUSTA", "LILIANA", "YOUNG", "CHRISTIAN", "LESSIE", "AMALIA", "SAVANNAH", "ANASTASIA", "VILMA", "NATALIA", "ROSELLA", "LYNNETTE", "CORINA", "ALFREDA", "LEANNA", "CAREY", "AMPARO", "COLEEN", "TAMRA", "AISHA", "WILDA", "KARYN", "CHERRY", "QUEEN", "MAURA", "MAI", "EVANGELINA", "ROSANNA", "HALLIE", "ERNA", "ENID", "MARIANA", "LACY", "JULIET", "JACKLYN", "FREIDA", "MADELEINE", "MARA", "HESTER", "CATHRYN", "LELIA", "CASANDRA", "BRIDGETT", "ANGELITA", "JANNIE", "DIONNE", "ANNMARIE", "KATINA", "BERYL", "PHOEBE", "MILLICENT", "KATHERYN", "DIANN", "CARISSA", "MARYELLEN", "LIZ", "LAURI", "HELGA", "GILDA", "ADRIAN", "RHEA", "MARQUITA", "HOLLIE", "TISHA", "TAMERA", "ANGELIQUE", "FRANCESCA", "BRITNEY", "KAITLIN", "LOLITA", "FLORINE", "ROWENA", "REYNA", "TWILA", "FANNY", "JANELL", "INES", "CONCETTA", "BERTIE", "ALBA", "BRIGITTE", "ALYSON", "VONDA", "PANSY", "ELBA", "NOELLE", "LETITIA", "KITTY", "DEANN", "BRANDIE", "LOUELLA", "LETA", "FELECIA", "SHARLENE", "LESA", "BEVERLEY", "ROBERT", "ISABELLA", "HERMINIA", "TERRA", "CELINA"]
first_male = ["JAMES", "JOHN", "ROBERT", "MICHAEL", "WILLIAM", "DAVID", "RICHARD", "CHARLES", "JOSEPH", "THOMAS", "CHRISTOPHER", "DANIEL", "PAUL", "MARK", "DONALD", "GEORGE", "KENNETH", "STEVEN", "EDWARD", "BRIAN", "RONALD", "ANTHONY", "KEVIN", "JASON", "MATTHEW", "GARY", "TIMOTHY", "JOSE", "LARRY", "JEFFREY", "FRANK", "SCOTT", "ERIC", "STEPHEN", "ANDREW", "RAYMOND", "GREGORY", "JOSHUA", "JERRY", "DENNIS", "WALTER", "PATRICK", "PETER", "HAROLD", "DOUGLAS", "HENRY", "CARL", "ARTHUR", "RYAN", "ROGER", "JOE", "JUAN", "JACK", "ALBERT", "JONATHAN", "JUSTIN", "TERRY", "GERALD", "KEITH", "SAMUEL", "WILLIE", "RALPH", "LAWRENCE", "NICHOLAS", "ROY", "BENJAMIN", "BRUCE", "BRANDON", "ADAM", "HARRY", "FRED", "WAYNE", "BILLY", "STEVE", "LOUIS", "JEREMY", "AARON", "RANDY", "HOWARD", "EUGENE", "CARLOS", "RUSSELL", "BOBBY", "VICTOR", "MARTIN", "ERNEST", "PHILLIP", "TODD", "JESSE", "CRAIG", "ALAN", "SHAWN", "CLARENCE", "SEAN", "PHILIP", "CHRIS", "JOHNNY", "EARL", "JIMMY", "ANTONIO", "DANNY", "BRYAN", "TONY", "LUIS", "MIKE", "STANLEY", "LEONARD", "NATHAN", "DALE", "MANUEL", "RODNEY", "CURTIS", "NORMAN", "ALLEN", "MARVIN", "VINCENT", "GLENN", "JEFFERY", "TRAVIS", "JEFF", "CHAD", "JACOB", "LEE", "MELVIN", "ALFRED", "KYLE", "FRANCIS", "BRADLEY", "JESUS", "HERBERT", "FREDERICK", "RAY", "JOEL", "EDWIN", "DON", "EDDIE", "RICKY", "TROY", "RANDALL", "BARRY", "ALEXANDER", "BERNARD", "MARIO", "LEROY", "FRANCISCO", "MARCUS", "MICHEAL", "THEODORE", "CLIFFORD", "MIGUEL", "OSCAR", "JAY", "JIM", "TOM", "CALVIN", "ALEX", "JON", "RONNIE", "BILL", "LLOYD", "TOMMY", "LEON", "DEREK", "WARREN", "DARRELL", "JEROME", "FLOYD", "LEO", "ALVIN", "TIM", "WESLEY", "GORDON", "DEAN", "GREG", "JORGE", "DUSTIN", "PEDRO", "DERRICK", "DAN", "LEWIS", "ZACHARY", "COREY", "HERMAN", "MAURICE", "VERNON", "ROBERTO", "CLYDE", "GLEN", "HECTOR", "SHANE", "RICARDO", "SAM", "RICK", "LESTER", "BRENT", "RAMON", "CHARLIE", "TYLER", "GILBERT", "GENE", "MARC", "REGINALD", "RUBEN", "BRETT", "ANGEL", "NATHANIEL", "RAFAEL", "LESLIE", "EDGAR", "MILTON", "RAUL", "BEN", "CHESTER", "CECIL", "DUANE", "FRANKLIN", "ANDRE", "ELMER", "BRAD", "GABRIEL", "RON", "MITCHELL", "ROLAND", "ARNOLD", "HARVEY", "JARED", "ADRIAN", "KARL", "CORY", "CLAUDE", "ERIK", "DARRYL", "JAMIE", "NEIL", "JESSIE", "CHRISTIAN", "JAVIER", "FERNANDO", "CLINTON", "TED", "MATHEW", "TYRONE", "DARREN", "LONNIE", "LANCE", "CODY", "JULIO", "KELLY", "KURT", "ALLAN", "NELSON", "GUY", "CLAYTON", "HUGH", "MAX", "DWAYNE", "DWIGHT", "ARMANDO", "FELIX", "JIMMIE", "EVERETT", "JORDAN", "IAN", "WALLACE", "KEN", "BOB", "JAIME", "CASEY", "ALFREDO", "ALBERTO", "DAVE", "IVAN", "JOHNNIE", "SIDNEY", "BYRON", "JULIAN", "ISAAC", "MORRIS", "CLIFTON", "WILLARD", "DARYL", "ROSS", "VIRGIL", "ANDY", "MARSHALL", "SALVADOR", "PERRY", "KIRK", "SERGIO", "MARION", "TRACY", "SETH", "KENT", "TERRANCE", "RENE", "EDUARDO", "TERRENCE", "ENRIQUE", "FREDDIE", "WADE", "AUSTIN", "STUART", "FREDRICK", "ARTURO", "ALEJANDRO", "JACKIE", "JOEY", "NICK", "LUTHER", "WENDELL", "JEREMIAH", "EVAN", "JULIUS", "DANA", "DONNIE", "OTIS", "SHANNON", "TREVOR", "OLIVER", "LUKE", "HOMER", "GERARD", "DOUG", "KENNY", "HUBERT", "ANGELO", "SHAUN", "LYLE", "MATT", "LYNN", "ALFONSO", "ORLANDO", "REX", "CARLTON", "ERNESTO", "CAMERON", "NEAL", "PABLO", "LORENZO", "OMAR", "WILBUR", "BLAKE", "GRANT", "HORACE", "RODERICK", "KERRY", "ABRAHAM", "WILLIS", "RICKEY", "JEAN", "IRA", "ANDRES", "CESAR", "JOHNATHAN", "MALCOLM", "RUDOLPH", "DAMON", "KELVIN", "RUDY", "PRESTON", "ALTON", "ARCHIE", "MARCO", "WM", "PETE", "RANDOLPH", "GARRY", "GEOFFREY", "JONATHON", "FELIPE", "BENNIE", "GERARDO", "ED", "DOMINIC", "ROBIN", "LOREN", "DELBERT", "COLIN", "GUILLERMO", "EARNEST", "LUCAS", "BENNY", "NOEL", "SPENCER", "RODOLFO", "MYRON", "EDMUND", "GARRETT", "SALVATORE", "CEDRIC", "LOWELL", "GREGG", "SHERMAN", "WILSON", "DEVIN", "SYLVESTER", "KIM", "ROOSEVELT", "ISRAEL", "JERMAINE", "FORREST", "WILBERT", "LELAND", "SIMON", "GUADALUPE", "CLARK", "IRVING", "CARROLL", "BRYANT", "OWEN", "RUFUS", "WOODROW", "SAMMY", "KRISTOPHER", "MACK", "LEVI", "MARCOS", "GUSTAVO", "JAKE", "LIONEL", "MARTY", "TAYLOR", "ELLIS", "DALLAS", "GILBERTO", "CLINT", "NICOLAS", "LAURENCE", "ISMAEL", "ORVILLE", "DREW", "JODY", "ERVIN", "DEWEY", "AL", "WILFRED", "JOSH", "HUGO", "IGNACIO", "CALEB", "TOMAS", "SHELDON", "ERICK", "FRANKIE", "STEWART", "DOYLE", "DARREL", "ROGELIO", "TERENCE", "SANTIAGO", "ALONZO", "ELIAS", "BERT", "ELBERT", "RAMIRO", "CONRAD", "PAT", "NOAH", "GRADY", "PHIL", "CORNELIUS", "LAMAR", "ROLANDO", "CLAY", "PERCY", "DEXTER", "BRADFORD", "MERLE", "DARIN", "AMOS", "TERRELL", "MOSES", "IRVIN", "SAUL", "ROMAN", "DARNELL", "RANDAL", "TOMMIE", "TIMMY", "DARRIN", "WINSTON", "BRENDAN", "TOBY", "VAN", "ABEL", "DOMINICK", "BOYD", "COURTNEY", "JAN", "EMILIO", "ELIJAH", "CARY", "DOMINGO", "SANTOS", "AUBREY", "EMMETT", "MARLON", "EMANUEL", "JERALD", "EDMOND", "EMIL", "DEWAYNE", "WILL", "OTTO", "TEDDY", "REYNALDO", "BRET", "MORGAN", "JESS", "TRENT", "HUMBERTO", "EMMANUEL", "STEPHAN", "LOUIE", "VICENTE", "LAMONT", "STACY", "GARLAND", "MILES", "MICAH", "EFRAIN", "BILLIE", "LOGAN", "HEATH", "RODGER", "HARLEY", "DEMETRIUS", "ETHAN", "ELDON", "ROCKY", "PIERRE", "JUNIOR", "FREDDY", "ELI", "BRYCE", "ANTOINE", "ROBBIE", "KENDALL", "ROYCE", "STERLING", "MICKEY", "CHASE", "GROVER", "ELTON", "CLEVELAND", "DYLAN", "CHUCK", "DAMIAN", "REUBEN", "STAN", "AUGUST", "LEONARDO", "JASPER", "RUSSEL", "ERWIN", "BENITO", "HANS", "MONTE", "BLAINE", "ERNIE", "CURT", "QUENTIN", "AGUSTIN", "MURRAY", "JAMAL", "DEVON", "ADOLFO", "HARRISON", "TYSON", "BURTON", "BRADY", "ELLIOTT", "WILFREDO", "BART", "JARROD", "VANCE", "DENIS", "DAMIEN", "JOAQUIN", "HARLAN", "DESMOND", "ELLIOT", "DARWIN", "ASHLEY", "GREGORIO", "BUDDY", "XAVIER", "KERMIT", "ROSCOE", "ESTEBAN", "ANTON", "SOLOMON", "SCOTTY", "NORBERT", "ELVIN", "WILLIAMS", "NOLAN", "CAREY", "ROD", "QUINTON", "HAL", "BRAIN", "ROB", "ELWOOD", "KENDRICK", "DARIUS", "MOISES", "SON", "MARLIN", "FIDEL", "THADDEUS", "CLIFF", "MARCEL", "ALI", "JACKSON", "RAPHAEL", "BRYON", "ARMAND", "ALVARO", "JEFFRY", "DANE", "JOESPH", "THURMAN", "NED", "SAMMIE", "RUSTY", "MICHEL", "MONTY", "RORY", "FABIAN", "REGGIE", "MASON", "GRAHAM", "KRIS", "ISAIAH", "VAUGHN", "GUS", "AVERY", "LOYD", "DIEGO", "ALEXIS", "ADOLPH", "NORRIS", "MILLARD", "ROCCO", "GONZALO", "DERICK", "RODRIGO", "GERRY", "STACEY", "CARMEN", "WILEY", "RIGOBERTO", "ALPHONSO", "TY", "SHELBY", "RICKIE", "NOE", "VERN", "BOBBIE", "REED", "JEFFERSON", "ELVIS", "BERNARDO", "MAURICIO", "HIRAM", "DONOVAN", "BASIL", "RILEY", "OLLIE", "NICKOLAS", "MAYNARD", "SCOT", "VINCE", "QUINCY", "EDDY", "SEBASTIAN", "FEDERICO", "ULYSSES", "HERIBERTO", "DONNELL", "COLE", "DENNY", "DAVIS", "GAVIN", "EMERY", "WARD", "ROMEO", "JAYSON", "DION", "DANTE", "CLEMENT", "COY", "ODELL", "MAXWELL", "JARVIS", "BRUNO", "ISSAC", "MARY", "DUDLEY", "BROCK", "SANFORD", "COLBY", "CARMELO", "BARNEY", "NESTOR", "HOLLIS", "STEFAN", "DONNY", "ART", "LINWOOD", "BEAU", "WELDON", "GALEN", "ISIDRO", "TRUMAN", "DELMAR", "JOHNATHON", "SILAS", "FREDERIC", "DICK", "KIRBY", "IRWIN", "CRUZ", "MERLIN", "MERRILL", "CHARLEY", "MARCELINO", "LANE", "HARRIS", "CLEO", "CARLO", "TRENTON", "KURTIS", "HUNTER", "AURELIO", "WINFRED", "VITO", "COLLIN", "DENVER", "CARTER", "LEONEL", "EMORY", "PASQUALE", "MOHAMMAD", "MARIANO", "DANIAL", "BLAIR", "LANDON", "DIRK", "BRANDEN", "ADAN", "NUMBERS", "CLAIR", "BUFORD", "GERMAN", "BERNIE", "WILMER", "JOAN", "EMERSON", "ZACHERY", "FLETCHER", "JACQUES", "ERROL", "DALTON", "MONROE", "JOSUE", "DOMINIQUE", "EDWARDO", "BOOKER", "WILFORD", "SONNY", "SHELTON", "CARSON", "THERON", "RAYMUNDO", "DAREN", "TRISTAN", "HOUSTON", "ROBBY", "LINCOLN", "JAME", "GENARO", "GALE", "BENNETT", "OCTAVIO", "CORNELL", "LAVERNE", "HUNG", "ARRON", "ANTONY", "HERSCHEL", "ALVA", "GIOVANNI", "GARTH", "CYRUS", "CYRIL", "RONNY", "STEVIE", "LON", "FREEMAN", "ERIN", "DUNCAN", "KENNITH", "CARMINE", "AUGUSTINE", "YOUNG", "ERICH", "CHADWICK", "WILBURN", "RUSS", "REID", "MYLES", "ANDERSON", "MORTON", "JONAS", "FOREST", "MITCHEL", "MERVIN", "ZANE", "RICH", "JAMEL", "LAZARO", "ALPHONSE", "RANDELL", "MAJOR", "JOHNIE", "JARRETT", "BROOKS", "ARIEL", "ABDUL", "DUSTY", "LUCIANO", "LINDSEY", "TRACEY", "SEYMOUR", "SCOTTIE", "EUGENIO", "MOHAMMED", "SANDY", "VALENTIN", "CHANCE", "ARNULFO", "LUCIEN", "FERDINAND", "THAD", "EZRA", "SYDNEY", "ALDO", "RUBIN", "ROYAL", "MITCH", "EARLE", "ABE", "WYATT", "MARQUIS", "LANNY", "KAREEM", "JAMAR", "BORIS", "ISIAH", "EMILE", "ELMO", "ARON", "LEOPOLDO", "EVERETTE", "JOSEF", "GAIL", "ELOY", "DORIAN", "RODRICK", "REINALDO", "LUCIO", "JERROD", "WESTON", "HERSHEL", "BARTON", "PARKER", "LEMUEL", "LAVERN", "BURT", "JULES", "GIL", "ELISEO", "AHMAD", "NIGEL", "EFREN", "ANTWAN", "ALDEN", "MARGARITO", "COLEMAN", "REFUGIO", "DINO", "OSVALDO", "LES", "DEANDRE", "NORMAND", "KIETH", "IVORY", "ANDREA"]

def create_student_data(stunum_start=111111, num_students=300):
    stunum = stunum_start
    students = []
    for i in range(num_students):
        stu = {'ID': stunum, 'First': '', 'Last': '', 'Email': ''}
        stunum += 1
        stu['First'] = random.choice(first_female) if random.random() < 0.35 else random.choice(first_male)
        stu['First'] = stu['First'].title()
        stu['Last'] = random.choice(last_names)
        email = stu['First'][0] + stu['Last']
        email = email.lower()
        email_available = False
        test_email = email
        count = 0
        while not email_available:
            if count > 0:
                test_email = email + str(count)
            if test_email in [s['Email'] for s in students]:
                count += 1
            else:
                email = test_email
                email = email.replace("'", '')
                email_available = True
        stu['Email'] = email
        students.append(stu)
    return students
    
def create_course_data(student_ids, num_assignments=7, num_exams=2):
    aweight = random.randint(3, 7)
    eweight = 10 - aweight
    amax = aweight * 100 // num_assignments
    emax = eweight * 100 // num_exams
    rows = []
    for sid in student_ids:
        mean_aptitude = random.uniform(0.4, 0.95)
        row = {'ID': sid, 'Total': 0}
        for i in range(num_assignments):
            val = min(amax, max(0, int(random.gauss(amax * mean_aptitude, amax * 0.1))))
            row['Assignment {}'.format(i+1)] = val
            row['Total'] += val
        for i in range(num_exams):
            val = min(emax, max(0, int(random.gauss(emax * mean_aptitude, emax * 0.1))))
            row['Exam {}'.format(i+1)] = val
            row['Total'] += val
        rows.append(row)
    return rows

def create_all_courses(num_courses, all_students, crn_start=99000):
    terms = ['Fall', 'Spring', 'Summer']
    years = ['2012', '2013', '2014', '2015', '2016']
    crn = crn_start
    course_meta = []
    for i in range(num_courses):
        num_students = random.randint(7, 25)
        students = random.sample(all_students, num_students)
        num_assignments = random.randint(2, 10)
        num_exams = random.randint(1, 4)
        course_data = create_course_data([s['ID'] for s in students], num_assignments, num_exams)
        course_meta.append({'ID': crn, 'Term': random.choice(terms), 'Year': random.choice(years), 'Size': num_students})
        with open('src/main/resources/courses/{}.csv'.format(crn), 'wb') as cfile:
            header = ['ID', 'Total'] + ['Assignment {}'.format(i+1) for i in range(num_assignments)] + ['Exam {}'.format(i+1) for i in range(num_exams)]
            cwriter = csv.DictWriter(cfile, header, quoting=csv.QUOTE_ALL)
            cwriter.writeheader()
            cwriter.writerows(course_data)
        crn += 1
    with open('src/main/resources/courses.csv', 'wb') as mfile:
        mwriter = csv.DictWriter(mfile, ['ID', 'Term', 'Year', 'Size'], quoting=csv.QUOTE_ALL)
        mwriter.writeheader()
        mwriter.writerows(course_meta)
  
students = create_student_data(num_students=300)
with open('src/main/resources/students.csv', 'wb') as stufile:
    swriter = csv.DictWriter(stufile, ['ID', 'First', 'Last', 'Email'], quoting=csv.QUOTE_ALL)
    swriter.writeheader()
    swriter.writerows(students)
        
create_all_courses(25, students)







        