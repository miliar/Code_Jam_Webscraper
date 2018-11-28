#include <bits/stdc++.h>
#define mp make_pair
#define ll long long


using namespace std;


int main()
{
    freopen("test.txt","r",stdin);
    freopen("test2.txt" , "w" , stdout);
    int T;
    scanf("%d",&T);
    for(int a = 1 ; a <= T ; a++)
    {
        int c , r;


        scanf("%d %d", &r,&c);
        char arr[r][c];
        vector<pair<int,int> > v;
        for(int i = 0 ; i < r ; i++)
        {

            string s;
            cin >> s;
//            cout << "here " << s << endl;
            for(int k = 0 ; k < c ;k++){
                if(s[k]!= '?')
                {
                    v.push_back(mp(i,k));
//                    cout << s[k] << " ---------->";
                }
                arr[i][k]=s[k];
            }

        }

        int indx=0 , indy = 0;
        for(int i = 0 ; i < v.size() ; i++)
        {
//            if(a==45)
//                cout <<"here";
            int x , y ;
            x= v[i].first;
            y = v[i].second;
            int x2 = v[i+1].first;
            int endd = r;
            for(int j = 0 ; j < v.size() ; j++)
            {
                if(j==i ) continue;
                if(v[j].first > x)
                    endd = min(endd, v[j].first);
            }
            if(i+1 < v.size() )
            {

                if(x < v[i+1].first)
                {
                    for(int k = indx ; k < endd ; k++)
                    {
                        for(int k2 = indy ; k2 < c ; k2++)
                            arr[k][k2] = arr[x][y];
                    }
                    indx = v[i+1].first;
                    indy=0;
                }
                else
                {
                    for(int k = indx ; k < endd ; k++)
                    {
                        for(int k2 = indy ; k2 < v[i+1].second  ; k2++)
                            arr[k][k2] = arr[x][y];
                    }
                    indy = v[i+1].second;
                }
            }
            else
            {
                for(int k = indx ; k < r ; k++)
                    {
                        for(int k2 = indy ; k2 < c ; k2++)
                            arr[k][k2] = arr[x][y];
                    }
            }

        }




        printf("Case #%d:\n",a );
        for(int i = 0 ; i < r ; i++)
        {
            for(int j = 0 ; j < c ; j++)
            {
                printf("%c",arr[i][j]);
            }
            printf("\n");
        }

    }
    printf("\n");

}
