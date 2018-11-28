#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

typedef long long ll;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define sz(t) ((int)(t.size())) 


int t,q = 1;
int n,p,R[52],Q[52][52],Left[52][52],Right[52][52];
vector < pair<int,int> > segments[52];
bool mark[52][52];



int main(){
	scanf("%d", &t);
	while(t){
		printf("Case #%d: ", q);
		cin>>n>>p;
		for(int i=0;i<n;i++) cin>>R[i];
		for(int i=0;i<n;i++){
			segments[i].clear();
			for(int j=0;j<p;j++){
				mark[i][j] = false;
				cin>>Q[i][j];
				if((10*Q[i][j])%(11*R[i]) == 0) Left[i][j] = (10*Q[i][j])/(11*R[i]);
				else Left[i][j] = (10*Q[i][j])/(11*R[i]) + 1;
				Right[i][j] = (10*Q[i][j])/(9*R[i]);

				if(Left[i][j] == 0) Left[i][j]++;

				if(Left[i][j] <= Right[i][j]) 
					segments[i].pb(mp(Left[i][j],Right[i][j]));
			}
		}
		if(n == 1){
			cout<<sz(segments[0])<<endl;
			t--;
			q++;
			continue;
		}
		int answ = 0;
		for(int i=0;i<n;i++) sort(segments[i].begin(),segments[i].end());
		int ind[52];
		for(int i=0;i<n;i++) ind[i] = 0;
		int mxr = -1, mnr = -1, mxl = -1, mnl = -1;

		while(true){
			bool z = true;
			for(int i=0;i<n;i++){
				if(ind[i] >= sz(segments[i])){
					z = false;
					break;
				}
			}
			if(!z) break;
			
			mnr = -1, mxl = -1;
			for(int i=0;i<n;i++){
				if(mnr == -1 || mnr > segments[i][ind[i]].second) mnr = segments[i][ind[i]].second;
				if(mxl == -1 || mxl < segments[i][ind[i]].first) mxl = segments[i][ind[i]].first;
			}
			if(mxl <= mnr){
				answ++;
				for(int i=0;i<n;i++) ind[i]++;
			}
			else{
				int h = 0,mnl = -1;
				for(int i=0;i<n;i++) 
					if(mnl == -1 || mnl > segments[i][ind[i]].first) 
						{mnl = segments[i][ind[i]].first; h = i;}
				ind[h]++;
			}
		}

		cout<<answ<<endl;
		t--;
		q++;
	}
	return 0;
}