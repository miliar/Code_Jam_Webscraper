#include <iostream>
#include <utility>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

inline unsigned long long max(unsigned long long a,unsigned long long b)
{
	return a>b?a:b;
}

inline unsigned long long min(unsigned long long a,unsigned long long b)
{
return a>b?b:a;
}

bool cmp(const pair<unsigned long long,unsigned long long>* p1,const pair<unsigned long long,unsigned long long>* p2)
{
	unsigned long long d1 = p1->second-p1->first-1;
	unsigned long long d2 = p2->second-p2->first-1;

	return d1>d2;
}

pair<unsigned long long,unsigned long long> *func(queue< pair<unsigned long long,unsigned long long>* >& q, unsigned long long k)
{
vector< pair<unsigned long long,unsigned long long>* > v;
unsigned long long t=q.size();
pair<unsigned long long,unsigned long long>* tmp;
unsigned long long mid,range,m1,m2,aux;

while(t--){
	v.push_back(q.front());
	q.pop();
}

sort(v.begin(),v.end(),cmp);

/**calculation of min max for final element**/
tmp = v[k-1];
range = tmp->second-tmp->first;
mid = range/2;
if(range%2!=0)
	mid++;

mid+=tmp->first;
m1 = mid-tmp->first-1;
m2 = tmp->second-mid-1;
aux = m1;
m1 = max(m1,m2);
m2 = min(aux,m2);
return new pair<unsigned long long,unsigned long long>(m1,m2);
}


pair<unsigned long long,unsigned long long> *findMM(unsigned long long n,unsigned long long k)
{
unsigned long long size=1,mid,range;
pair<unsigned long long,unsigned long long>* tmp=NULL;
queue< pair<unsigned long long,unsigned long long>* > q;

if(n==k)
	return new pair<unsigned long long,unsigned long long>(0,0);


q.push(new pair<unsigned long long,unsigned long long>(0,n+1));
    
    while(size < k){
       while(size > 0){
       	tmp = q.front();
       	q.pop();
        range = tmp->second-tmp->first-1;
        mid = range/2;
        if(range%2 != 0)
        	mid++;
        mid+=tmp->first;
       	q.push(new pair<unsigned long long,unsigned long long>(tmp->first,mid));
       	q.push(new pair<unsigned long long,unsigned long long>(mid,tmp->second));
       	delete tmp;
       	k--;
       	size--;
       }
       size = q.size();
    }
 
return func(q,k);
}


int main()
{
	int t;
	unsigned long long n,k;
	pair<unsigned long long,unsigned long long>* tmp;
	int c=0;
	cin >> t;

	while(t--){
		c++;
		cin >> n >> k;
		tmp = findMM(n,k);
		cout <<"Case #" << c <<": " << tmp->first <<" " <<tmp->second << endl; //first->max , second->min
	}

    
}