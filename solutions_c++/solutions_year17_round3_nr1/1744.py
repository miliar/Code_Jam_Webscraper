#include <QFile>
#include <QTextStream>
#include <QStringList>

#define M_PI 3.14159265358979323846264338327950288419716939937510L

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2017/Round1C/A/A-large.in");
QFile outFile("C:/CodeJam2017/Round1C/A/output.txt");

class Pancake {
public:
  Pancake(long double r, long double h): R(r), H(h) {};
  long double R, H;
};

bool pancakeTaller(const Pancake &p1, const Pancake &p2) {
     return p1.R*p1.H > p2.R*p2.H;
}

int main(int argc, char *argv[])
{
  inFile.open(QFile::ReadOnly);
  outFile.open(QFile::WriteOnly);
  QTextStream inData(&inFile);
  QTextStream outData(&outFile);

  int T;
  inData >> T;

  for(int t=0; t<T; t++) {
    int N, K;
    inData >> N;
    inData >> K;

    QList<Pancake> cakes;

    for (int i=0; i<N; i++) {
      int R, H;
      inData >> R;
      inData >> H;
      cakes.append(Pancake(R, H));
    }

    qSort(cakes.begin(), cakes.end(), pancakeTaller);

    long double tSh = 0, tMaxR = 0;

    for (int i=0; i<(K-1); i++) {
      tMaxR = qMax(tMaxR, cakes[i].R);
      tSh += 2 * M_PI * cakes[i].R * cakes[i].H;
    }

    long double maxS = 0;

    for (int i=K-1; i<N; i++) {
      long double maxR = qMax(tMaxR, cakes[i].R);
      long double tS = tSh + 2*M_PI*cakes[i].R*cakes[i].H + M_PI*maxR*maxR;
      if (tS > maxS) maxS = tS;
    }


    outData << QString("Case #%1: %2\r\n").arg(t+1).arg( maxS, 0, 'f', 9 );
  }
}









