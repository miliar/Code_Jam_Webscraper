#include <bits/stdc++.h>
using namespace std;
int CountSteps(string &str,int k)
{
    int n = str.length();
    int flip[n];
    int head=0,tail=0,count=0;
    for(int i=0;i<n;i++)
    {
        if(head!=tail && flip[tail] <= i-k)
        tail ++;
        int size = head - tail;
        if((size % 2 == 0 && str[i] == '-') || (size % 2 == 1 && str[i] == '+'))
        {
            if(i > n-k)
            return -1;
            count++;
            flip[head++] = i;
        }
    }
    return count;
}
int main() 
{
	int T,Case = 1;
	cin >> T;
	while(T--)
	{
	    int K;
	    string str;
	    cin>>str>>K;
	    int steps = CountSteps(str,K);
	    
	    if(steps == -1)
	    cout<<"Case #"<<Case<<": IMPOSSIBLE"<<endl;
	    else
	    cout<<"Case #"<<Case<<": "<<steps<<endl;
	    
	    Case++;
	}
	return 0;
}
