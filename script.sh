for f in /var/lib/mysql/[insert name of database here]/*.csv
do
    mysql -e "LOAD DATA INFILE '"$f"' INTO TABLE [nameoftable] 
      FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES" 
      -u [username] --password= [password] [name of database]
echo "Done: '"$f"' at $(date)"
done
