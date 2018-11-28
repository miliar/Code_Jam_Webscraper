#include <QFile>
#include <QTextStream>
#include <QVector>
#include <QMap>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2017/Qualification/C/C-large.in");
QFile outFile("C:/CodeJam2017/Qualification/C/output.txt");


int main(int argc, char *argv[])
{
  inFile.open(QFile::ReadOnly);
  outFile.open(QFile::WriteOnly);
  QTextStream inData(&inFile);
  QTextStream outData(&outFile);

  int T;
  inData >> T;

  for (int t=0; t<T; t++) {
    qint64 N, K;
    inData >> N;
    inData >> K;

    QMap<qint64, qint64> intervals;
    intervals.insert(N, 1);
    qint64 biggest_interval, biggest_interval_amount;
    qint64 Ls, Rs;

    while (K > 0) {
      biggest_interval = intervals.lastKey();
      biggest_interval_amount = intervals.last();
      intervals.remove(biggest_interval);

      biggest_interval--; // occupy one stall
      Ls = biggest_interval / 2;
      Rs = biggest_interval - Ls;

      K -= biggest_interval_amount;
      if (K <= 0) break;

      intervals.insert(Ls, intervals.value(Ls,0) + biggest_interval_amount);
      intervals.insert(Rs, intervals.value(Rs,0) + biggest_interval_amount);
    }

    outData << QString("Case #%1: %2 %3\r\n").arg(t+1).arg(qMax(Ls,Rs)).arg(qMin(Ls,Rs));
  }
}
