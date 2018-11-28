#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstdlib>
#include <stdio.h>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <utility>
#include <math.h>
#define for0(i,n) for(int i=0; i<n; i++)
#define for1(i,n) for(int i=1; i<n; i++)
#define FOR(i,o,n,s) for(int i=o; i<n; i+=s)
#define refor0(i,n) for(int i=n-1; i>=0; i--)
#define pb push_back

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
	int dataNum;
	cin >> dataNum;

	int i, j, k;
	int stall;
	int people;
	FOR(i, 0, dataNum, 1) {
		cin>>stall;
		cin>>people;
		int step=ceil(log2(people+1));
		//cout<<step<<endl;
		int max1=stall;
		int min1=0;
		FOR(j, 0, step-1, 1) {
			min1=(max1-1)/2;
			max1=max1-1-min1;
			//cout<<max1<<" "<<min1<<endl;
		}

		int max2=stall;
		int min2=0;
		FOR(j, 0, step-1, 1) {
			if(j!=0) max2=min2;
			min2=(max2-1)/2;
			max2=max2-1-min2;
			//cout<<max2<<" "<<min2<<endl;
		}

		int ttlMax=max(max1, max2);
		int ttlMin=min(min1, min2);
		/*if(stall%2==0 && max1==min1) 
			ttlMin=min1-1;
		else
			ttlMin=min1;*/

		//cout<<step<<" "<<ttlMax<<" "<<ttlMin<<endl;
		int empty=pow(2, step-1);
		int residue=stall-(empty-1);
		int p_residue=people-(empty-1);
		if(ttlMax==ttlMin) {
			ttlMin=(ttlMax-1)/2;
			ttlMax=ttlMax-1-ttlMin;
		} else {
			int num=(empty*ttlMin-residue)/(ttlMin-ttlMax);
			//cout<<residue<<" "<<num<<endl;
			if(num>=p_residue) {
				ttlMin=(ttlMax-1)/2;
				ttlMax=ttlMax-1-ttlMin;			
			} else {
				int tmpMin=ttlMin;
				ttlMin=(ttlMin-1)/2;
				ttlMax=tmpMin-1-ttlMin;
			}
		}

		cout<<"Case #"<<i+1<<": "<<ttlMax<<" "<<ttlMin<<endl;
	}
}