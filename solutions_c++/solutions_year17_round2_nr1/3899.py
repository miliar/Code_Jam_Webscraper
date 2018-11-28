#include <QFile>
#include <QTextStream>
#include <QStringList>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2017/Round1B/A/A-large.in");
QFile outFile("C:/CodeJam2017/Round1B/A/output.txt");

class Horse {
public:
  Horse(double new_pos, double new_speed) {
    position = new_pos;
    speed = new_speed;
  }

  double position, speed;
};

bool horseFarther(const Horse &h1, const Horse &h2)
{
     return h1.position < h2.position;
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
    double D;
    int N;
    inData >> D;
    inData >> N;

    QList<Horse> horses;

    for (int i=0; i<N; i++) {
      double t_point, t_speed;
      inData >> t_point;
      inData >> t_speed;
      horses << Horse(t_point, t_speed);
    }

    qSort(horses.begin(), horses.end(), horseFarther);

    double total_time = 0;
    for (int i=0; ;) {
      double intersect_point = D;
      int intersect_index = N;

      for (int j=i+1; j<N; j++) {
        if (horses[i].speed == horses[j].speed) continue;
        double intersect_time = (horses[j].position + horses[j].speed * total_time - horses[i].position) / (horses[i].speed - horses[j].speed);
        if (intersect_time < 0) continue;

        double t_intersect_point = horses[i].position + horses[i].speed * intersect_time;
        if (t_intersect_point < intersect_point) {
          intersect_point = t_intersect_point;
          intersect_index = j;
        }
      }

      total_time += (intersect_point - horses[i].position) / horses[i].speed;

      if (intersect_index == N) break;

      i = intersect_index;
      horses[i].position = intersect_point;
    }

    outData << QString("Case #%1: %2\r\n").arg(t+1).arg( D / total_time, 0, 'f', 9 );
  }
}
