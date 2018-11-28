//
//  main.cpp
//  ProblemA
//
//  Created by 胡思源 on 2017/4/8.
//  Copyright © 2017年 胡思源. All rights reserved.
//

#include<set>
#include<vector>
#include <iostream>

using namespace std;

int len;

string converse(string a)
{
    string result="";
    for (int i=len-1;i>=0;i--)
        result+=a[i];
    return result;
}

string flip(string a, int index, int k)
{
    string result=a;
    for (int i=index;i<=index+k-1;i++)
        result[i]=result[i]=='+'?'-':'+';
    return result;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    
    int T;
    cin>>T;
    int count=0;
    while (++count<=T)
    {
        set<string> book;
        vector<string> q;
        vector<int> step;
        
        string input;
        int K;
        cin>>input;
        cin>>K;
        len=input.size();
        
        string target="";
        for (int i=0;i<len;i++)
            target+='+';
        
        int s=-1,t=0;
        q.push_back(input);
        book.insert(input);
        book.insert(converse(input));
        step.push_back(0);
        
        if (input==target)
        {
            cout<<"Case #"<<count<<": 0"<<endl;
            continue;
        }
        
        bool flag=false;
        while (s<t)
        {
            s++;
            string x=q[s];
            int ste=step[s];
            for (int i=0;i<=len-K;i++)
            {
                string str=flip(x, i, K);
                if (str==target)
                {
                    cout<<"Case #"<<count<<": "<<ste+1<<endl;
                    flag=true;
                    break;
                }
                if (book.find(str)==book.end())
                {
                    t++;
                    q.push_back(str);
                    book.insert(str);
                    book.insert(converse(str));
                    step.push_back(ste+1);
                }
            }
            
            if (flag)
                break;
        }
        
        if (!flag)
            cout<<"Case #"<<count<<": IMPOSSIBLE"<<endl;
        
    }
    return 0;
}
