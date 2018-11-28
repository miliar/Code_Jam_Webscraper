#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
//#include<bits/stdc++.h>
using namespace std;
int main ()
 { 
 freopen("B-small-attempt1.in","r",stdin);
 freopen("B-small-attempt1.out","w",stdout);
 
 ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.precision(10);
    cout << fixed;
    int T;
    cin >> T;
    for(int tc=1;tc<=T;tc++)
{
	cout << "\nCase #" << tc << ": ";
	 	long long int n,i;
		long long int check=0,checkf=0,temp;
	 long long int count=0,countif=0;
 	cin>>n;
	 	for(i=n;i>=1;i--)
	 	{
		 temp=i;
	 	checkf=10;
 	while(temp>0){
 		count++;
 		check=temp%10;	
 		temp=temp/10;
 		if(checkf>=check)
	 {
	 checkf=check;
	 	countif++;
	 	}
	 else{
	 break;
	 	}
	 }
if(count==countif)
{
	cout<<i;
	break;
}
else{
	count=0;
	countif=0;

}
}}
return 0;
}

	 
