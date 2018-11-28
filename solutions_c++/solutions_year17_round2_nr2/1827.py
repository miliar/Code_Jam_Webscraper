#include <bits/stdc++.h>
using namespace std;

bool mycomapre(const pair<int,char> &l,const pair<int,char> &r)
{
    return l.first > r.first ;
}
int main() {
	int t;
	cin>>t;
	int count = 1;
	while(t--)
	{
	    int n;
	    int R,O,Y,G,B,V;
	    
	    cin>>n>>R>>O>>Y>>G>>B>>V;
	    vector<pair<int,char> >  A;
	    
	    A.push_back(make_pair(R,'R'));
	    A.push_back(make_pair(O,'O'));
	    A.push_back(make_pair(Y,'Y'));
	    A.push_back(make_pair(G,'G'));
	    A.push_back(make_pair(B,'B'));
	    A.push_back(make_pair(V,'V'));
	    sort(A.begin(),A.end(),mycomapre);
	    
	    /*for(int i=0;i<6;i++)
	    {
	        cout<<A[i].first<<" "<<A[i].second<<endl;
	    } */
	    int sz = A[0].first;
	    vector<vector<char> > ans(sz);
	    for(int i=0;i<sz;i++)
	    {
	        ans[i].push_back(A[0].second);
	    }
	    
	    int j = 1;
	    int i =0;
	    while(1)
	    {
	        if(j == 6)
	        break;
	        
	        while(A[j].first)
	        {
	            if(i == sz)
	            i = 0;
	            ans[i].push_back(A[j].second);
	             i++ ;
	            A[j].first -= 1;
	        }
	        j++ ;
	       
	    }
	    
	    string q = "";
	    for(int i=0;i<A[0].first;i++)
	    {
	        for(int j =0;j<ans[i].size();j++)
	        q += ans[i][j];
	    }
	    
	    cout<<"Case #"<<count++<<": ";
	    
	    if(q[0] == q[q.length() -1 ])
	    cout<<"IMPOSSIBLE\n";
	    else
	    cout<<q<<endl;
	}
	return 0;
}
