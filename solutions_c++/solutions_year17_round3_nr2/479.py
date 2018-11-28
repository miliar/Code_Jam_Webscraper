#include <cstdio>
#include <vector>
#include <algorithm>
#include <climits>
#include <cstdlib>
#include <queue>
#include <map>
#define ii pair<int,int>
#define ll long long
const long double PI=3.1415926535;

using namespace std;

bool cmp(int a, int b) {
	return b<a;
}

int main(){
	int t,a1,a2,risultato=0, turno[1440],lavoro1,lavoro2;
	vector<int> blocchi11,blocchi12,blocchi22;
	ii in1,in2;
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt","w");
	
	fscanf(in,"%d", &t);
	for(int i=0; i<t; i++) {
		blocchi11.resize(0);
		blocchi12.resize(0);
		blocchi22.resize(0);
		fscanf(in,"%d %d",&a1,&a2);
		lavoro1=lavoro2 = risultato= 0;
		for(int k=0;k<1440; k++) {
				turno[k] = 0;
			}
		for(int j=0; j<a1; j++) {
			fscanf(in, "%d %d",&(in1.first),&(in1.second));
			for(int k=in1.first;k<in1.second; k++) {
				turno[k] = 2;
				lavoro2++;
			}
		}
		for(int j=0; j<a2; j++) {
			fscanf(in, "%d %d",&(in2.first),&(in2.second));
			for(int k=in2.first;k<in2.second; k++) {
				turno[k] = 1;
				lavoro1++;
			}
		}
		
		/*for(int j = 0; j<1440; j++) {
			if(turno[j]!=0 && turno[(j+1)%1440]!=turno[j])
				risultato++;
		}*/
		
		for(int j=0; j<1440; j++) {
			if(turno[j] == 1 && turno[(j+1)%1440]==0) {
				int l=1;
				for(; turno[(j+l)%1440]==0; l++);
				if(turno[(j+l)%1440]==1)
					blocchi11.push_back(l-1);
				else
					blocchi12.push_back(l-1);
			}
			if(turno[j] == 2 && turno[(j+1)%1440]==0) {
				int l=1;
				for(; turno[(j+l)%1440]==0; l++);
				if(turno[(j+l)%1440]==2)
					blocchi22.push_back(l-1);
				else
					blocchi12.push_back(l-1);
			}
			if(turno[j] == 1 && turno[(j+1)%1440]==2)
				blocchi12.push_back(0);
			else if(turno[j] == 2 && turno[(j+1)%1440]==1)
				blocchi12.push_back(0);
		}
		
		risultato +=blocchi12.size();
		
		sort(blocchi11.begin(), blocchi11.end(),cmp);
		sort(blocchi22.begin(), blocchi22.end(),cmp);
		//sort(blocchi12.begin(), blocchi12.end());
		while(lavoro1<720 && blocchi11.size()>0) {
			if(blocchi11[blocchi11.size()-1]<=720-lavoro1) {
				lavoro1 += blocchi11[blocchi11.size()-1];
				blocchi11.pop_back();
			} else {
				blocchi11[blocchi11.size()-1]-=720-lavoro1;
				lavoro1=720;
			}
		}
		while(blocchi11.size()>0) {
			lavoro2+=blocchi11[blocchi11.size()-1];
			blocchi11.pop_back();
			risultato+=2;
		}
		
		while(lavoro2<720 && blocchi22.size()>0) {
			if(blocchi22[blocchi22.size()-1]<=720-lavoro2) {
				lavoro2 += blocchi22[blocchi22.size()-1];
				blocchi22.pop_back();
			} else {
				blocchi22[blocchi22.size()-1]-=720-lavoro2;
				lavoro2=720;
			}
		}
		while(blocchi22.size()>0) {
			lavoro1+=blocchi22[blocchi22.size()-1];
			blocchi22.pop_back();
			risultato+=2;
		}
		
		fprintf(out,"Case #%d: %d\n",i+1,risultato);
	}
	return 0;
}
