#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool decim(const pair<long long int,long long int> &a,
              const pair<long long int,long long int> &b)
	      {
	          return (a.first > b.first);
		  }


int main()
{
long long int t;
cin >> t;
for(int avc=1;avc<=t;avc++)
{
long long int m,n;
cin >> m >> n;
long long int d,e;
vector< pair<long long int,long long int> > mn;
long long int a[m][2];
vector< pair<long long int,long long int> > rr;
for(int i= 0;i<m;i++){
cin >> d >> e;
a[i][0]=d;
a[i][1]=e;
rr.push_back( make_pair(d*d,i));
mn.push_back( make_pair(2*d*e,i));
}
sort(mn.begin(),mn.end(),decim);
sort(rr.begin(),rr.end(),decim);
long long int max=0;
//long long int index=-1;
long long int flag = 0;
for(int i=0;i<n;i++)
{
long long int z;
z = a[mn[i].second][0];
z= z*z;
if(max < z)
max = z;
//index = mn[i].second;}
}
//cout << "hi"<<mn[n-1].first<<endl;
for(int i= 0;i<m;i++)
{
if(max >= rr[i].first)
break;
else {
//cout << "poty"<<index<<endl;
if(max + mn[n-1].first < rr[i].first + 2*a[rr[i].second][0]*a[rr[i].second][1])
{
//cout << rr[i].first + 2*a[rr[i].second][0]*a[rr[i].second][1]<<endl;
 mn[n-1].first =  2*a[rr[i].second][0]*a[rr[i].second][1];
 //cout << mn[n-1].first<<endl;
 mn[n-1].second=  i;
 flag = 1;
 break;
}

}
}
double sum = 0;
for(int i =0;i<n;i++){
sum += mn[i].first;
//cout << mn[i].first<<endl;
}
//cout << rr[mn[n-1].second]
if(flag)
sum += rr[mn[n-1].second].first;
else
sum += max;
double fsum = sum;
cout << fixed;
double finalsum = fsum*3.14159265358979323846;
cout <<"Case #"<<avc<<":"<<" ";
cout << setprecision(8)<<finalsum<<"\n";
//for(int i=0;i<m;i++)
//cout << mn[i].first <<" "<< mn[i].second<<"\n";
}
}
