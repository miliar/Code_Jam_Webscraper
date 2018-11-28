#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("output.txt","w",stdout); 
	int t;
	cin >> t;
	for( int i = 1; i <= t; i++ ){
		int num , flag = 1;;
		scanf("%d", &num);
		if( num < 10 ){
			printf("Case #%d: %d\n", i , num );
			continue;
		}
		while( 1 > 0 ){
			int temp = num;
			vector<int> a;
			while( temp > 0 ){
				int l = temp % 10;
				a.push_back(l);
				temp /= 10;
			}
			flag = 1;
			for( int j = 0; j < a.size() - 1; j++ ){
				if( a[j] < a[j + 1] ){
					flag = 0;
					break;
				}
			}
			if( flag == 1 ){
				break;
			}
			num--;
		}
		printf("Case #%d: %d\n", i , num );
	}
}