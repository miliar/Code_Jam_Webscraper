#include <cstdio>
#include <queue>

using namespace std;

const int max_n = 101;

int maxdist[max_n];
int speed[max_n];

int dist[max_n][max_n];
int n, q;


struct state {
	double time;
	int city;
	int speed;
	int dist_left;
};

struct cmp {
	   bool operator() (const state &a, const state &b) {
		   return a.time > b.time || (a.time == b.time && a.speed < b.speed);
	   }
};


void procroute() {
	int a, b;
	int arrival[max_n];

	priority_queue<state, vector<state>, cmp> pq;
	for (int i = 0; i < n; i++) arrival[i] = -1;

	scanf("%d %d", &a, &b);

	a--; b--;

//	printf("A %d %d\n", a, b);
	state tmp;

	tmp.time = 0;
	tmp.city = a;
	tmp.speed = 0;
	tmp.dist_left = 0;
	pq.push(tmp);

	while(!pq.empty()) {
		tmp = pq.top();
		pq.pop();

//		printf("Time %lf c %d\n", tmp.time, tmp.city);
	

		if(tmp.city == b) {
		
			printf("%f ", tmp.time);
			return;
		}


		arrival[tmp.city] = tmp.time;

		for (int i = 0; i < n; i++) {
			int d = dist[tmp.city][i];
			if (i != tmp.city && d > -1) {
				state tmp2;
				tmp2.city = i;
			
				if (d <= tmp.dist_left) {
					tmp2.time = tmp.time + (double)(d) / (double) tmp.speed;
					tmp2.dist_left = tmp.dist_left - d;
					tmp2.speed = tmp.speed;
					pq.push(tmp2);
				}

				// change
				tmp2.time = tmp.time + (double)d / (double)speed[tmp.city];
				tmp2.dist_left = maxdist[tmp.city] - d;
				tmp2.speed = speed[tmp.city];
				pq.push(tmp2);
			}
		}
		
	}

	printf("%f ", arrival[b]);
}

void proc(int caseno) {
	scanf("%d %d", &n, &q);
	for (int i = 0; i < n; i++)
		scanf("%d %d", &maxdist[i], &speed[i]);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf("%d", &dist[i][j]);

	printf("Case #%d: ", caseno);
	for (int i = 0; i < q; i++)
		procroute();

	printf("\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
		proc(i + 1);
}
