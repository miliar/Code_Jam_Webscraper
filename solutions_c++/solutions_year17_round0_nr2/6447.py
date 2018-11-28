/*************************************************************************
    > File Name: TidyNumbers.cpp
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 六  4/ 8 16:56:57 2017
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int judge(long long a)
{
	int b[20] ;
	for(int i = 0; i < 20; i++)
	{
		long long tmp = pow(10,i) ;
		b[i] = ((long long)(a / tmp)) % 10 ;
	}
	for(int i = 0; i < 19; i++)
		if(b[i] < b[i + 1])
			return 0 ;
	return 1 ;
}
int main()
{
	freopen("out.out","w",stdout) ;
	freopen("in.in","r",stdin) ;
	int t ;
	cin >> t ;
	for(int i = 0; i < t; i++)
	{
		long long n ;
		cin >> n ;
		long long x = 1 ;
		int count = 1 ;
		while(judge(n) == 0)
		{
			n -= x ;
			if(x != 1)
			{
				n = n / x * x ;
				long long tmp ;
				for(int j = 0; j < count - 1; j++)
				{
					tmp = 9 * pow(10,j) ;
					n += tmp ;
				}
			}
			x *= 10 ;
			count ++ ;
		}
		printf("Case #%d: ",i + 1) ;
		cout << n << endl ;
	}
	return 0 ;
}
