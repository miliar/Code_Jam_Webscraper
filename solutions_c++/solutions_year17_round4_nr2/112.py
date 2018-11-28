#include <stdio.h>
#include <string.h>

int ticks[1010][1010]; //person, seat
int persons[1010];
int seats[1010];
int Np; //num person
int Ns; //num seat

int main(){
	int jcase;
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		memset(ticks, 0, sizeof(ticks));
		memset(persons, 0, sizeof(persons));
		memset(seats, 0, sizeof(seats));
		
		scanf("%d %d", &Ns, &Np);
		int Nt;
		scanf("%d", &Nt);
		
		for(int i=0; i<Nt; i++){
			int where, who;
			scanf("%d %d", &where, &who);
			ticks[who][where]++;
			persons[who]++;
			seats[where]++;
		}
		
		int minRides = 0;
		for(int i=1; i<=Np; i++){
			if(persons[i] > minRides) minRides = persons[i];
		}
		int leftOver = 0;
		for(int i=1; i<=Ns; i++){
			leftOver += minRides;
			leftOver -= seats[i];
			if(leftOver < 0){
				while(leftOver < 0){
					leftOver += i;
					minRides++;
				}
			}
		}
		
		int numPro = 0;
		for(int i=1; i<=Ns; i++){
			if(seats[i] > minRides) numPro += (seats[i] - minRides);
		}
		
		printf("Case #%d: %d %d\n", icase+1, minRides, numPro);
		
		//fprintf(stderr, "case %d/%d\n", icase+1, jcase);
	}
	return 0;
}
