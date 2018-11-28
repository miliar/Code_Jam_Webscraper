#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <iostream>
#include <queue>
using namespace std;
vector< pair<int,int> > vv;
priority_queue<double> area;
int main(){
	int T;
	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("out.txt","w");
	fscanf(in,"%d",&T);
	for(int o=1;o<=T;o++){
		vv.clear();
		int N,K;
		fscanf(in,"%d %d",&N,&K);
		for(int i=0;i<N;i++){
			int r,h;
			fscanf(in,"%d %d",&r,&h);
			vv.push_back(make_pair(r,h));
		}
		
		sort(vv.begin(),vv.end());
		double M = 0;
		//scanf(" ");
		for(int i=0;i<N;i++){
			int r = vv[i].first;
			int h = vv[i].second;
			if(area.size()>=K-1){
				double sum = M_PI*r*r + 2*M_PI*r*h;
				vector<double> temp;
				for(int j=0;j<K-1;j++){
					sum += area.top();
					temp.push_back(area.top());
					area.pop();
				}
				for(int i=0;i<temp.size();i++)
					area.push(temp[i]);
				temp.clear();
				M = max(M,sum);
			}
			area.push(2*M_PI*r*h);
		}
		fprintf(out,"Case #%d: %.9lf\n",o,M);
		while(area.size())
			area.pop();
	}
	return 0;
}