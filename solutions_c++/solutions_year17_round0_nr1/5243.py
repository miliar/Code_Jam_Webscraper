#include<bits/stdc++.h>

using namespace std;

void preProcess(unordered_map<string,int> &umap,int len,int k)
{
    string s;
    queue<pair<string,int> > myqueue;
    for(int i=0;i<len;i++)
    {
        s=s+"+";
    }
    myqueue.push(make_pair(s,0));
    while(!myqueue.empty())
    {
        pair<string,int> tempPair=myqueue.front();
        myqueue.pop();
        string temps=tempPair.first;
        if(umap.find(temps)!=umap.end())
        {
            continue;
        }
        //cout<<"m "<<temps<<endl;
        umap[temps]=tempPair.second;
        for(int i=0;i<=(len-k);i++)
        {
            string temps2=temps;
            for(int j=0;j<k;j++)
            {
                if(temps2[i+j]=='+')
                {
                    temps2[i+j]='-';
                }
                else
                {
                    temps2[i+j]='+';
                }
            }
            myqueue.push(make_pair(temps2,tempPair.second+1));
        }
    }
}
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int ans,k;
        string s;
        unordered_map<string,int> umap;
        cin>>s>>k;
        preProcess(umap,s.length(),k);/*
        for (auto& elem: umap) std::cout << " " << elem.first << ":" << elem.second<<endl;*/
        if(umap.find(s)==umap.end())
        {
         cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";   
        }
        else
        {
        cout<<"Case #"<<i<<": "<<umap[s]<<"\n";
        }
    }
    return 0;
}