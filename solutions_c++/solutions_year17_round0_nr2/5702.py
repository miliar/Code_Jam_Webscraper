#include <bits/stdc++.h>
#include<string.h>

using namespace std;

int main() {
    long long int N,i,temp,minimum,res;
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int tt,T,K,count,qq,length,A[20],B[20];

  cin >> T;
  for (int qq = 1; qq <= T; qq++)
  {
        cin >> N;
        length=0;
        temp=N;
        int d=0;
        while(temp)
        {
            A[d++]=temp%10;
            length++;
            temp=temp/10;
        }

        for(int j=length;j>0;j--)
        {
            B[length-j]=A[j-1];
        }
            while(1)
            {
                int f=0;
                for(int i=0;i<length-1;i++)
                {
                    if(B[i]>B[i+1])
                    {
                        B[i]--;
                        for(int j=i+1;j<=length-1;j++)
                        B[j]=9;
                        f=1;
                    }
                }
                if(f==0)
                break;
            }

            printf("Case #%d: ", qq);
            for(int i=0;i<length;i++){
            if(B[i]!=0)
            cout << B[i];

            }
            cout << endl;



  }

  return 0;
}


