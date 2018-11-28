#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define F first
#define S second
#define all(v) v.begin(),v.end()
#define make0(a) memset(a,0,sizeof(a))
#define make1(a) memset(a,-1,sizeof(a))

const int mod = 1e9+7;
 
const int MAX_CHAR = 26;
 
struct Key
{
    int freq; // store frequency of character
    char ch;
    bool operator<(const Key &k) const
    {
        return freq < k.freq;
    }
};
 
void rearrangeString(string str)
{

    int n = str.length();
 
    int count[MAX_CHAR] = {0};
    for (int i = 0 ; i < n ; i++)
    {
        count[str[i]-'A']++;
    }
    priority_queue< Key > pq;
    for (char c = 'A' ; c <= 'Z' ; c++)
        if (count[c-'A'])
            pq.push( Key { count[c-'A'], c} );
 
    str = "" ;
    Key prev {-1, '#'} ;
    while (!pq.empty())
    {
        // pop top element from queue and add it
        // to string.
        Key k = pq.top();
        pq.pop();
        str = str + k.ch;
        // IF frequency of previous character is less
        // than zero that means it is useless, we
        // need not to push it
        if (prev.freq > 0)
            pq.push(prev);
 
        // make current character as the previous 'char'
        // decrease frequency by 'one'
        (k.freq)--;
        prev = k;
    }

    if(str[0] == str[n-1])
    {
    	for(int i=1;i<n;i++)
    	{
    		if(str[i] != str[0] and str[i+1] != str[0])
    		{
    			for(int j=n-2;j>=i+1;j--)
    			{
    				str[j+1] = str[j];
    			}
    			str[i+1] = str[0];
    			break;
    		}
    	}
    }
    cout << str << endl;
    // int ct=0;
    // for(int i=0;i<n;i++)
    // {
    // 	if(str[i] == 'Y')
    // 		ct++;
    // }
    // cout << ct << endl;
    assert(str[0] != str[n-1]);
}

int main()
{
	int T;
	cin >> T;
	for(int f=1;f<=T;f++)
	{
		cout << "Case #" << f << ": ";
		int N;
		cin >> N;
		int R,O,Y,G,B,V;
		cin >> R >> O >> Y >> G >> B >> V;
		if(R > N/2 or Y > N/2 or B > N/2)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}
		string s = "";
		for(int i=0;i<R;i++)
			s += "R";
		for(int i=0;i<B;i++)
			s += "B";
		for(int i=0;i<Y;i++)
			s += "Y";
		rearrangeString(s);

	}
	return 0;
}