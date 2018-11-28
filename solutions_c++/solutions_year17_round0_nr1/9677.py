#include <bits/stdc++.h>
using namespace std;
bool comp(vector<char>vec)
{
    for(int i = 0 ; i < vec.size() ; ++i)
    {
        if(vec[i]=='-')
            return false;
    }
    return true;
}
int main()
{
    int tc,c=0;
    scanf("%d",&tc);
    while(tc--)
    {
        string s;
        int k,v=0;
        cin>>s;
        scanf("%d",&k);
        vector<char> vec;
        for(int i = 0; i < s.size(); ++i)
        {
            vec.push_back(s[i]);
        }
        for(int i = 0; i < vec.size(); ++i)
        {
//            cout<<"i: "<<i<<" "<<vec[i]<<endl;
//            for(int p = 0 ; p < vec.size(); ++p)
//            {
//                cout<<vec[p];
//            }
//            cout<<endl;
            if(comp(vec))
            {
                printf("Case #%d: %d\n",++c,v);
                break;
            }
            else
            {
                if(vec[i]=='-')
                {
//                    cout<<"Entro"<<endl;
                    if(i+k <= vec.size())
                    {
                        ++v;
                        for(int j = 0; j < k ; ++j)
                        {
                            if(vec[i+j]=='-')
                                vec[i+j]='+';
                            else
                                vec[i+j]='-';
                        }

                    }
                }
            }
        }
        if(!comp(vec))
            printf("Case #%d: IMPOSSIBLE\n",++c);
    }
}
