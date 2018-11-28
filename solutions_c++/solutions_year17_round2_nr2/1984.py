#include <bits/stdc++.h>
using namespace std;
FILE *fi;

int jat(int g)
{

    fi=fopen("ez.txt","at");
    int k,s[6];
    string ss,ki="ROYGBV";
    cin>>k>>s[0]>>s[1]>>s[2]>>s[3]>>s[4]>>s[5];
    int kez,ln=-1;
    for (int i=0; i<6; i+=2)
    {
        if (s[i]>ln)
        {
            ln=s[i];
            kez=i;
        }
    }
    ln=-1;
    s[kez]--;
    ss+=ki[kez];
    int el=kez,ab=kez;
    for (int i=1; i<k; i++)
    {

        for (int j=0; j<6; j+=2)
        {
            if (s[j]>ln  &&j!=el)
            {
                ln=s[j];
                kez=j;
            }
            else if (s[j]==ln && j==ab && j!=el)
            {
                ln=s[j];
                kez=j;
            }

        }

      // cout<<kez<<endl;
        if (ln<=0)
        {
            fprintf(fi,"Case #%d: IMPOSSIBLE\n",g+1);
            fclose(fi);
            return 0;
        }
        ln=-1;
        s[kez]--;
        ss+=ki[kez];
        el=kez;
    }
if (ss[k-1]==ss[0])
        {
            fprintf(fi,"Case #%d: IMPOSSIBLE\n",g+1);
            fclose(fi);
            return 0;
        }


    fprintf(fi,"Case #%d: ",g+1);
    for (int i=0;i<k;i++) fprintf(fi,"%c",ss[i]);
    fprintf(fi,"\n");
    fclose(fi);
    return 0;
}
int main()
{
    fi=fopen("ez.txt","wt");
    fclose(fi);
    int n;
    scanf("%d",&n);

    for (int i=0; i<n; i++)
    {

        jat(i);
    }
    return 0;
}
