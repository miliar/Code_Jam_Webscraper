//  Created by Chlerry in 2017.
//  Copyright (c) 2017 Chlerry. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define Size 1000010
#define ll long long
#define mk make_pair
#define pb push_back
#define mem(array, x) memset(array,x,sizeof(array))
typedef pair<int,int> P;

double K[1010],S[1010];

int main()
{
    // freopen("in.txt","r",stdin);
    int T;cin>>T;
    double D,ans;
    int N;
for(int ca=0;ca<T;ca++)
{
	cin>>D>>N;
	cin>>K[0]>>S[0];
	ans=D*S[0]/(D-K[0]);
	for(int i=1;i<N;i++)
	{
		cin>>K[i]>>S[i];
		ans=min(ans,D*S[i]/(D-K[i]));
		// printf(">> %.6lf\n",D*S[i]/(D-K[i]));
	}
	printf("Case #%d: %.6lf\n",ca+1,ans);
}
    return 0;
}
