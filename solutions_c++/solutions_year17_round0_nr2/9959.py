#include<iostream>
#include<cstdio>
using namespace std;
int T;

int main()
{
    freopen("B-small-attempt1.in","r", stdin);
	freopen("B-small-attempt1.out","w", stdout);
    cin >> T ;
    int T0 = T;
    long long n,n0;
    int a[19];
    long long be = 0;


    while(T--)
        {
            cin>>n ;
            n0 = n ;
            be = 0;
            bool flag = 0;
            for(int i = 0 ; i <18 ; i++)
            {
                a[i]= n0 % 10;
                n0 /= 10;
            }

            int FNZ = 17;
            int aa,aaa;
            for(int i = 17 ; i >=0 ; i-- )
            {
                if( a[i] != 0)
                {
                    FNZ = i;
                    aa = a[i];
                    break;
                }
            }
            //cout<< FNZ+1<<"  "<<endl ;
            int NZ=FNZ+1;

            while(NZ--)
            {
                aaa = a[NZ+1];
                aa=a[NZ];
                int cha = aa - aaa;
                //cout<<aaa<<" "<<aa<<"  NZ = "<<NZ;

                for(int i0 = NZ ; i0 >= 0 ; i0-- )
            {
                be = be +cha;
                cha *= 10;
            }
                //cout<<"be = "<<be<<endl;
                if(n <  be)
                {
                    a[NZ] = a [NZ] - 1;
                    for(int i = NZ-1 ; i >= 0 ; i--)
                        a[i] = 9;
                    break;
                }
            }
            int SFNZ;
            if(a[FNZ]==0)
                SFNZ = FNZ -1;
            else
                SFNZ = FNZ;
            cout<<"Case #"<<T0 - T<<": ";
            for(int j = SFNZ; j >=0  ;j--)
            {
                cout<<a[j];
            }
            cout<<endl;
        }
    return 0;
}
