#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {

    int t;
    int caso = 1;
    double d;
    int n;
    double horseSpeed;
    double horseDist;
    double speed = 0;
    double slowHorseDist;
    double slowHorseSpeed;
    double tempo;

    scanf("%d\n", &t);

    for (int i = 0; i < t; i++) {

      scanf("%lf %d", &d, &n);

      for (int j = 0; j < n; j++) {

        scanf("%lf %lf", &horseDist, &horseSpeed);

        tempo = (d - horseDist)/horseSpeed;
        if(tempo > speed) {
          slowHorseSpeed = (d - horseDist)/horseSpeed;
          speed = tempo;
        }

      }

      printf("Case #%d: %.6lf\n", caso, d/slowHorseSpeed);

	  speed = 0;
	  caso++;

    }

}
