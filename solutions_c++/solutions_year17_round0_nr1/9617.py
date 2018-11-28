#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[]) {
  int TEST_FROM = 0;
  int TEST_TO = 123456789;
  if (argc == 3) {
    sscanf(argv[1], "%d", &TEST_FROM);
    sscanf(argv[2], "%d", &TEST_TO);
  }
  //freopen("small.in", "r", stdin);
  //freopen("small.out", "w", stdout);
  freopen("large.in", "r", stdin);
  freopen("large.out", "w", stdout);

  int tt, ans=0, l, i, j, sum, k;
  string pancake;
  int m[1001];
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {

    //---------------------------------------------------------------------------------------------
    // input data starts
    //---------------------------------------------------------------------------------------------

    cin>>pancake>>k;

    sum=0;
    ans=0;
    l=pancake.length();
    for (i=0;i<l;i++)
    {
        if (pancake[i]=='+')
        {
            m[i]=0;
        }
        else
        {
            m[i]=1;
        }
        sum+=m[i];
    }

    //---------------------------------------------------------------------------------------------
    // input data ends
    //---------------------------------------------------------------------------------------------
                    if (qq < TEST_FROM || qq > TEST_TO) {
                        continue;
                    }
                    printf("Case #%d: ", qq);
                    fflush(stdout);
    //---------------------------------------------------------------------------------------------
    // solution starts
    //---------------------------------------------------------------------------------------------

    if (sum==0) {ans=0;}
    else
    {

        for (i=0;i<l-(k-1);++i)
        {
            if (m[i]==1)
            {
                ++ans;
                for (j=0;j<k;++j)
                {
                    if (m[i+j]==1)
                    {
                        m[i+j]=0;
                        --sum;
                    }
                    else
                    {
                        m[i+j]=1;
                        ++sum;
                    }
                }

            }

        }

    }

        //cout<<endl<<"Sum: "<<sum;
        //cout<<endl<<"Ans: "<<ans;
        //cout<<endl;
    if (sum==0)
    {
        printf("%d\n", ans);
    }
    else
    {
        cout<<"IMPOSSIBLE\n";
    }


    //---------------------------------------------------------------------------------------------
    // solution ends
    //---------------------------------------------------------------------------------------------

    fflush(stdout);
    fprintf(stderr, "test %d solved, time = %d ms\n", qq, (int)clock());
  }
  return 0;
}
