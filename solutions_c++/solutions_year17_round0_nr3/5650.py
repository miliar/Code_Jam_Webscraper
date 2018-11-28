#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	int jj;
	for(jj=0;jj<t;jj++)
	{
		vector <int> ans;
		int n;
		int i,k;
		scanf("%d",&n);
		ans.push_back(n);
		
		int y,z;
		scanf("%d",&k);
		for(i=0;i<k;i++)
		{
			int x,index=0;
				x = ans[0];
				index++;
			x--;
			y = ceil((float)x/2);
			z = x/2;
		//	printf("x %d y %d z %d\n",x,y,z);
			ans.push_back(y);
			ans.push_back(z);
			int ww;
			ans.erase(ans.begin());
			
			sort(ans.begin(),ans.end());
			reverse(ans.begin(),ans.end());
					}
		int a1= ans.size()-1,a2 = a1-1;
		printf("Case #%d: %d %d\n",jj+1,y,z);
		ans.erase(ans.begin(),ans.begin()+ans.size()-1);
	}
	// your code goes here
	return 0;
}