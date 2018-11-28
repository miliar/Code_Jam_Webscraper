#pragma GCC optimize ("O2")

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include <iomanip> 

#define small 
//#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::vector<double> vd;
typedef std::vector<vd> vvd;
typedef long long ll;
typedef unsigned long long ull;

const int E = 0, S = 1, T = 2;


int main()
{
#if defined(small)
  freopen("C-small-attempt2.in", "r", stdin);
#elif defined(large)
  freopen("C-large.in", "r", stdin);
#endif
  freopen("out.out", "w", stdout);

  int TC;
  scanf("%d", &TC);
  std::cerr << TC << " testcases\n";

  for (int i = 1; i <= TC; i++) {
    int N, Q;
    scanf("%d %d", &N, &Q);
    vvd horses;
    for (int j = 0; j < N; j++) {
      vd horse(2);
      scanf("%lf %lf", &horse[E], &horse[S]);
      horses.push_back(horse);
    }
    vi nextCity(N), distToNext(N);
    for (int org = 0; org < N; org++) {
      int dist;
      for (int dest = 0; dest < N; dest++){
	scanf("%d", &dist);
	if (dist != -1){
	  nextCity[org] = dest;
	  distToNext[org] = dist;
	}
      }
    }
    for (int q = 0; q < Q; ++q){
      int u, v;
      scanf("%d %d", &u, &v);
    }

    //debug
    std::cerr << "horses: ";
    for (auto horse : horses) std::cerr << "\n" << horse[E] << " " << horse[S];
    std::cerr << "\n";
    std::cerr << "connections: ";
    for (int j = 0; j < N; ++j) std::cerr << nextCity[j] << "(" << distToNext[j] << ")" << " ";
    std::cerr << "\n";


    
  

    int city = 0;
    vvd activeHorses;
    vd horse(3);
    horse[E] = horses[0][E];
    horse[S] = horses[0][S];
    std::cerr << "lbl1 " << horse.size() << " " << T << "\n";
    horse[T] = 0;
    std::cerr << "lbl2\n";
    activeHorses.push_back(horse);
    
    while(city != N-1){
      std::cerr << "city: " << city << "\n";
      for (int h = 0; h < activeHorses.size(); ++h){
	std::cerr << "\n h! E: " << activeHorses[h][E] << " T: " << activeHorses[h][T];
	activeHorses[h][E] -= distToNext[city];
	if (activeHorses[h][E] < 0){
	  activeHorses.erase(activeHorses.begin()+h);
	  --h;
	  std::cerr << " removed";
	  continue;
	}
	activeHorses[h][T] += distToNext[city]/activeHorses[h][S];
	std::cerr << "   | new:  E: " << activeHorses[h][E] << " T: " << activeHorses[h][T];
      }
      ++city;
      horse[E] = horses[city][E];
      horse[S] = horses[city][S];
      double minTime = 10e12;
      for (auto &hor : activeHorses) 
	minTime = std::min(minTime, hor[T]);
      horse[T] = minTime;
      activeHorses.push_back(horse);
      std::cerr << "\n";
    }

    double minTime = 10e12;
    for (auto &horse : activeHorses) 
      minTime = std::min(minTime, horse[T]);

    std::cout << "Case #" << i << ": " << std::setprecision(6) << std::fixed << minTime << "\n";
    std::cerr << "Case #" << i << ": " << std::setprecision(6) << std::fixed << minTime << "\n";

  }
  
  printf("\n");
  fprintf(stderr, " \n");

  return 0;
}
