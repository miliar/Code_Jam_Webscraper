#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int w =0;w<t;++w)
    {
        string n;
        cin>>n;
        for(int i=atoi(n.c_str()); i>0; --i)
        {
            int cont=1;

            if(n.length()==1)
            {
                cout<<"Case #"<<w+1<<": "<<n<<endl;
                break;
            }
            else
            {
                bool flag=true;
                for(int h = 0; h<n.length()-1; ++h)
                {
                    if(h!=n.length())
                    {
                        if(n[h]> n[h+1])
                        {
                            flag =false;
                            break;
                        }
                    }
                }
                if(flag)
                {
                    cout<<"Case #"<<w+1<<": "<<n<<endl;
                    break;
                }
            }
            int z = atoi(n.c_str());
            char* c = new char;
            itoa(z-1,c,10);
            string cat(c);
            n = cat;
        }
    }
    return 0;
}
