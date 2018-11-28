#include <bits/stdc++.h>
using namespace std;

vector<int> num;
void pre()
{
    int l=0,m=1;
    for(int i=1; i<100; )
    {
        if(i%10==0)
        {
            l++;
            i+=l;
        }
        else
        {
            num.push_back(i);
            i++;
        }
    }
    for(int i=100; i<1005; )
    {
        if(i%100==0)
        {
            i+=m*10;
            l=(m-1);
            m++;
        }
        else if(i%10==0)
        {
            l++;
            i+=l;
        }
        else
        {
            num.push_back(i);
            i++;
        }
    }
}

int main() {
	// your code goes here
	pre();
	
	int test;
	cin>>test;
	for(int i=0; i<test; i++)
	{
	    int n, pos;
	    cin>>n;
	    vector<int>::iterator it;
	    it=upper_bound(num.begin(), num.end(), n);
	    pos=(it-num.begin());
	    cout<<num[pos-1]<<endl;
	}
	
	return 0;
}
