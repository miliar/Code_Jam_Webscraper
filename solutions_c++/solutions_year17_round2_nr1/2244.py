#include<algorithm>
#include<cassert>
#include<cstring>
#include<iostream>
#include<list>
#include<map>
#include<set>
#include<sstream>
#include<string>
#include<unordered_map>
#include<unordered_set>
#include<utility>
#include<vector>

#define NN 1000

using LL = long long int;
using namespace std;

int cas, ca;

double D;
int N;
double pos;
double sp;
void main2() {
  cin>>D>>N;
  double t = -2;
  for (int i=0; i<N; ++i ) {
    cin>>pos>>sp;
    t = max(t, (D-pos)/sp);
  }
  printf("%.7f\n", D/t);


}

int main(int argc, char *argv[]) {
	cin>>cas;
  bool showtime = argc > 1;
  time_t starttime = 0;
  if (showtime) {
    time(&starttime);
  }
	for(ca = 1; ca<=cas; ++ca) {
    if (showtime) {
      cerr<<ca<<"/"<<cas<<" "<<time(NULL) - starttime<<endl;
    }
		cout<<"Case #"<<ca<<": ";
    main2();
	}
}
