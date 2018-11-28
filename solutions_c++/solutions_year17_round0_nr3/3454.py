#include<iostream>
#include<queue>
#include<cstdlib>

using namespace std;

bool before(pair<unsigned long long,unsigned long long> a,pair<unsigned long long,unsigned long long> b)
{
  unsigned long long da=a.second-a.first;
  unsigned long long db=b.second-b.first;
	if(da>db) return false;
  if(da==db && a.first < b.first) return false;
  return true;
}
int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
  {
    unsigned long long n,k;
    priority_queue<pair<unsigned long long,unsigned long long>, vector<pair<unsigned long long,unsigned long long> >, decltype(&before)> pq(&before);
    cin >> n >> k;
    pq.push(make_pair(0,n+1));
    for(unsigned long long i=1;i<k;i++)
    {
      pair<unsigned long long, unsigned long long> p = pq.top();
      pq.pop();
      unsigned long long l = p.first;
      unsigned long long r = p.second;
      unsigned long long m = (r-l)/2+l;
      pq.push(make_pair(l,m));
      pq.push(make_pair(m,r));
    }
    pair<unsigned long long, unsigned long long> p = pq.top();
    unsigned long long l = p.first;
    unsigned long long r = p.second;
    unsigned long long m = (r-l)/2+l;
    unsigned long long max,min;
    if(m-l-1 > r-m-1){max=m-l-1;min=r-m-1;}
    else{max=r-m-1;min=m-l-1;}
    cout << "Case #" << t << ": " << max << " " << min << endl;
  }
  return 0;
}
