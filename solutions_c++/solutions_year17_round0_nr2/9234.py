#include <bits/stdc++.h>
#include<string.h>

using namespace std;
void printArray(int A[],int l)
{
    for(int i=0;i<l;i++)
    cout << A[i];
    cout << endl;
}
int main() {
    long long int Num,i,tem,mini,res;
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  int tt,T,K,count,qq,digilen,A[20],B[20];

  cin >> T;
  for (int qq = 1; qq <= T; qq++)
  {
        cin >> Num;
        digilen=0;
        tem=Num;
        int d=0;
        while(tem)
        {
            A[d++]=tem%10;
            digilen++;
            tem=tem/10;
        }
        //printArray(A,digilen);
        for(int j=digilen;j>0;j--)
        {
            B[digilen-j]=A[j-1];
        }
        //printArray(B,digilen);
        //cout << digilen;
        mini=(pow(10,digilen)-1)/9;
        if(Num<mini){
                    res=pow(10,digilen-1)-1;
                    printf("Case #%d: ", qq);
                    cout << res << endl;
        }
        else
        {
            while(1)
            {
                int f=0;
                for(int i=0;i<digilen-1;i++)
                {
                    if(B[i]>B[i+1])
                    {
                        B[i]--;
                        for(int j=i+1;j<=digilen-1;j++)
                        B[j]=9;
                        f=1;
                    }
                }
                if(f==0)
                break;
            }
            printf("Case #%d: ", qq);
            for(int i=0;i<digilen;i++){
            if(B[i]!=0)
            cout << B[i];

            }
            cout << endl;
        }


  }

  return 0;
}


