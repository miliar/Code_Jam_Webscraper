#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2017/Qualification/B/B-large.in");
QFile outFile("C:/CodeJam2017/Qualification/B/output.txt");


int main(int argc, char *argv[])
{
  inFile.open(QFile::ReadOnly);
  outFile.open(QFile::WriteOnly);
  QTextStream inData(&inFile);
  QTextStream outData(&outFile);

  int T;
  inData >> T;

  for (int t=0; t<T; t++) {
    QString str;
    inData >> str;

    for (int i=str.count()-2; i>=0; i--) {
      if (str[i] > str[i+1]) { //decrease and fill the rest with '9'
        str[i] = QString("%1").arg(str[i].digitValue() - 1)[0];
        for (int j=i+1; j<str.count(); j++) str[j] = '9';
      }
    }

    int first_dig = 0;
    for ( ; first_dig < str.count() && str[first_dig]=='0'; first_dig++) ;

    outData << QString("Case #%1: %2\r\n").arg(t+1).arg(str.mid(first_dig));
  }
}
