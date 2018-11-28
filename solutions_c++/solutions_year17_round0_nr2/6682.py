    #include <iostream>
    #include<fstream>

    int NumString[20];
    using namespace std;

    void stclr()
    {
        for(int i=0;i<20;++i)
            NumString[i]=-1;
    }
    int main()
    {
        int t,i,j,flag=1,x=1;
        long long a;
        /*
        freopen("B-small-attempt0.in","r",stdin);
        freopen("a.out","w",stdout);*/
        cin>>t;
        for(int z=0;z<t;++z)
        {
            cin>>a;
            i=0;
            stclr();
            while(a)
            {
                for(j=19;j>0;--j)
                    NumString[j]=NumString[j-1];
                NumString[0]=a%10;
                a/=10;
            }
            while(1)
            {
                for(i=1;NumString[i]!=-1;++i)
                    if(NumString[i]<NumString[i-1])
                        break;

                if(NumString[i]==-1)
                    break;

                --NumString[i-1];
                for(int o=i;NumString[o]!=-1;++o)
                    NumString[o]=9;

                if(i==1&&NumString[0]==0)
                {
                    for(j=0;NumString[j+1]!=-1;++j)
                        NumString[j]=9;
                    NumString[j]=-1;
                }
            }

            a=0;
            for(i=0;NumString[i]!=-1;++i)
                a=a*10+NumString[i];
            cout<<"Case #"<<z+1<<": "<<a<<endl;
        }
        return 0;
    }
