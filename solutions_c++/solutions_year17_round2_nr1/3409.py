#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>

#define LL long long
#define ULL unsigned long long
#define PI 3.14159265

#define FILE_NAME "A-large"

using namespace std;

static int dx[] = {-1,-1,-1,0,0,1,1,1};
static int dy[] = {-1,0,1,-1,1,-1,0,1};

int main()
{
#ifdef D
	char filename[256];
	sprintf(filename, "%s.in", FILE_NAME);
	freopen(filename, "r", stdin);
	sprintf(filename, "%s.out", FILE_NAME);
	freopen(filename, "w", stdout);
#endif
	
	int case_num, no=1;
	cin>>case_num;

	while(no<=case_num){
		int Dest, N, K, S;
		double maxHour=0.0;
		
		cin>>Dest>>N;
		// cout<<Dest<<" "<<N<<endl;
		for(int i=0;i<N;i++){
			cin>>K>>S;
			// cout<<K<<" "<<S<<endl;
			double tempHour = (double)(Dest-K)/S;
			if(tempHour>maxHour){
				maxHour = tempHour;
			}
		}
		// cout<<"maxHour: "<<maxHour<<endl;
		
		cout.precision(6);
		cout.setf(ios::fixed, ios::floatfield);
		cout<<"Case #"<<no<<": "<<(Dest/maxHour);
		cout<<endl;
		no++;
	}

#ifdef D
	fclose(stdin);
	fclose(stdout);
#endif
	
	return 0;
}