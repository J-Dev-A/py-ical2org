query=$(icalBuddy -npn -iep "title,datetime" -ps "| : |" -po "datetime,title"  -ic "Calendar" -nc eventsToday)
for i in $query;
do
  lines=${i%$'-'*}
  for line in $lines;
  do
    echo $line
    echo 'hi'
  done
done
