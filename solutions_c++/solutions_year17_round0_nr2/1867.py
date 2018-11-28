#include <bits/stdc++.h>
#define ii pair<int, int>
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vii vector< pair<int, int> >
typedef long long ll;
using namespace std;
char s[100];
char res[100];
int n;
int solve()
{
    bool bad = 0;
    for(int i = 0; i+1< n; i++)
    {
        if(s[i]<= s[i+1])
        {
            res[i] = s[i];
        }
        else
        {
            res[i] = s[i]-1;
            for(int j = i+1; j< n; j++) res[j] = '9';
            bad = 1;
            break;
        }
    }
    if(!bad) res[n-1] = s[n-1];
    for(int i = 0; i< n; i++) s[i] = res[i];
    for(int i = 0; i+1< n; i++) if(s[i]> s[i+1]) return 0;
    return 1;
}
int main()
{
    int tt;
    scanf("%d", &tt);
    for(int qq = 1; qq<= tt; qq++)
    {
        double clock_start = clock();
        scanf("%s", s);
        n = strlen(s);
        printf("Case #%d: ", qq);
        while(!solve());
        bool lead = 0;
        for(int i = 0; i< n; i++)
        {
            if(res[i] == '0' && lead == 0)
            {
                lead = 1; continue;
            }   
            printf("%c", res[i]);
        }
        printf("\n");
        fprintf(stderr, "Test %d solved in %.2lf s.\n", qq, (clock()-clock_start)/CLOCKS_PER_SEC);
    }
	return 0;
}
