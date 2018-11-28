#include<iostream>
#include<algorithm>
#include<map>
#include<vector>

using namespace std;

#define MAX_SIZE 1001
#define PI 3.141592653589793238462643383279502884L

int T;
int N, K;
map<int, int> cakes;
long double D[MAX_SIZE][MAX_SIZE];
int last[MAX_SIZE][MAX_SIZE];

template <typename T1, typename T2>
struct less_second {
  typedef pair<T1, T2> type;
  bool operator ()(type const& a, type const& b) const {
	return a.first > b.first;
  }
};


int main() {
  FILE * inFile;
  //inFile = fopen ("input.txt","r");
  inFile = fopen ("A-small-attempt1.in","r");
  inFile = fopen ("A-large.in","r");
  FILE * outFile;
  outFile = fopen ("output.txt","w");

  //scanf("%d", &T); 
  fscanf(inFile, "%d", &T); 

  for(int i = 0; i < T; i++) {
	cakes.clear();

	long double ans = 0;

	//scanf("%d %d", &N, &K);
	fscanf(inFile, "%d %d", &N, &K);

	for(int j = 0; j < MAX_SIZE; j++) {
	  for(int k = 0; k < MAX_SIZE; k++) {
		D[j][k] = 0;
		last[j][k] = -1;
	  }
	}

	int R, H;
	vector<pair<int, int> > mapcopy;
	for(int j = 0; j < N; j++) {
	  //scanf("%d %d", &R, &H);
	  fscanf(inFile, "%d %d", &R, &H);
	  mapcopy.push_back(pair<int, int>(R, H));
	}

	sort(mapcopy.begin(), mapcopy.end(), less_second<int, int>());

	for(int j = 0; j < mapcopy.size(); j++) {
	  pair<int, int>cake = mapcopy[j];

	  //printf("%d -> %d\n", cake.first, cake.second);
	}

	for(int j = 0; j < N; j++) {
	  pair<int, int>cake = mapcopy[j];
	  long double rr = (long double)cake.first;
	  long double hh = (long double)cake.second;

	  D[1][j] = rr * rr * PI + (long double)2 * PI * rr * hh;
	}

	for(int j = 2; j <= K; j++) {
	  for(int k = 1; k < N; k++) {
		pair<int, int>cake = mapcopy[k];
	  long double rr = (long double)cake.first;
	  long double hh = (long double)cake.second;
		int lastK = last[j][k-1];

		long double left = 0;

		if(lastK >= 0) {
		  long double rr2 = (long double)mapcopy[lastK].first;
		  long double hh2 = (long double)mapcopy[lastK].second;

		  left = D[j][k-1] + (long double)2 * PI * rr * hh;
		  left -= ((long double)2 * PI * rr2 * hh2);
		}

		long double right = D[j-1][k-1] + (long double)2 * PI * rr * hh;;

		//printf("%Lf %Lf %Lf\n", D[j-1][k-1], left, right);

		if(D[j][k] > left && D[j][k] > right) {
		}
		else {
		  last[j][k] = k;
		  if(left > right) {
			D[j][k] = left;
		  }
		  else {
			D[j][k] = right;
		  }
		}
	  }
	}

	ans = D[K][0];
	for(int j = 0; j < N; j++) {
	  if(D[K][j] > ans) {
		ans = D[K][j];
	  }
	}
	//printf("Case #%d: %0.8Lf\n", i + 1, ans);
	fprintf(outFile, "Case #%d: %0.9Lf\n", i + 1, ans);
	//cout << ans << endl;
  }

  printf("%Lf\n", PI);

  return 0;
}

