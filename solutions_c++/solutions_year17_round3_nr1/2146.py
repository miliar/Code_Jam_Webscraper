/*
 * A.cc
 *
 *  Created on: 30 de abr de 2017
 *      Author: david
 */




/*
 * A.cc
 *
 *  Created on: 30 de abr de 2017
 *      Author: david
 */


#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#define SZ(x) (int)(x).size()
#define ALL(x) (x).begin(),(x).end()
#define _USE_MATH_DEFINES


using namespace std;


int main(){
	freopen("A.in","r",stdin);
	freopen("As.out","w",stdout);
	int test_cases;
	cin>>test_cases;

	for (int test_case = 0; test_case < test_cases; ++test_case) {
		vector<pair<long long, long long> > pancakes;
		long long N,K;
		cin>>N>>K;
		for (int i = 0; i < N; ++i) {
			long long R, H;
			cin>>R>>H;
			pancakes.push_back(make_pair(R,H));
		}
		sort(ALL(pancakes));
		reverse(ALL(pancakes));

		long long resp = 0;
		for (int i = 0; i < (1<<N); ++i) {
			int cont = 0;
			vector<pair<long long,long long> > temp;
			for (int j = 0; j < N; ++j) {
				if (i & (1<<j)){
					temp.push_back(pancakes[j]);
					cont++;
				}
			}
			long long pos_resp=0;
			if (cont == K){
				for (int j = 0; j < K-1; ++j) {
					pos_resp+= (temp[j].first*temp[j].first - temp[j+1].first*temp[j+1].first ) + 2 * temp[j].first * temp[j].second;

				}
				pos_resp+=(temp[K-1].first*temp[K-1].first ) + 2 * temp[K-1].first  * temp[K-1].second;
				resp= max(resp, pos_resp);
			}

		}
		double finalresp = resp*1.0*4*atan(1);
		printf("Case #%d: %.7lf\n",test_case+1,finalresp);
		//cout<<"Case #"<<test_case+1<<": "<<resp<<endl;

	}
	return 0;
}



