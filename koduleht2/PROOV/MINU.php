<html>
<head>
<title>TSAUKS</title>
</head>
<body>
<h1>MIS ON? On 2017 veebruar 11</h1>
<?php //see siin ongi serveri poolel, PHP tag ?>
<?php echo "see tulebki php scriptist - HOLA DUDE"; ?>

<?php 
    $host = "localhost";
    $user = "test";
    $pass = "t3st3r123";
    $db = "test";

    $l = mysqli_connect($host, $user, $pass, $db);
    mysqli_query($l, "SET CHARACTER SET UTF8") or
            die("Error, ei saa andmebaasi charsetti seatud");
    
    mysqli_close($l);
?>

</body>
</html>
