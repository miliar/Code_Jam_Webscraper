#include <QFile>
#include <QTextStream>
#include <QStringList>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2017/Round1/A/A-large.in");
QFile outFile("C:/CodeJam2017/Round1/A/output.txt");


int main(int argc, char *argv[])
{
  inFile.open(QFile::ReadOnly);
  outFile.open(QFile::WriteOnly);
  QTextStream inData(&inFile);
  QTextStream outData(&outFile);

  int T;
  inData >> T;

  for(int t=0; t<T; t++) {
    int R, C;
    inData >> R;
    inData >> C;

    QStringList lines;
    int first_non_empty_line = -1;
    for (int i=0; i<R; i++) {
      QString tStr;
      inData >> tStr;

      int first_non_empty_letter = tStr.indexOf(QRegExp("[^?]"), 0);
      if (first_non_empty_letter >= 0) {
        if (first_non_empty_line==-1) first_non_empty_line = i;
        for (int j=0; j<first_non_empty_letter; j++) tStr[j] = tStr[first_non_empty_letter];

        for (int j=first_non_empty_letter + 1; j<tStr.length(); j++) {
          if (tStr[j]=='?') tStr[j] = tStr[j-1];
        }
      }

      lines.append(tStr);
    }

    for (int i=0; i<first_non_empty_line; i++) {
      lines[i] = lines[first_non_empty_line];
    }

    for (int i=1; i<R; i++) {
      int first_non_empty_letter = lines[i].indexOf(QRegExp("[^?]"), 0);
      if (first_non_empty_letter < 0) lines[i] = lines[i-1];
    }

    outData << QString("Case #%1:\r\n").arg(t+1);
    for (int i=0; i<R; i++) {
      outData << lines[i] << "\r\n";
    }
  }
}
