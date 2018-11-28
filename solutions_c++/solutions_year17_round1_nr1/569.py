#include <iostream>
#include<fstream>
#include <vector>
#include <string>
using namespace std;

int main()
{

    FILE *fin = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/Round1/1A/A-large.in", "r", stdin);
	FILE *fout = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/Round1/1A/A-large.out", "w", stdout);
    int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
        int R,C;
        char x;
        cin>>R>>C;
        vector<char> P;
        char k[R][C];
        for(int i=0; i<R; i++)
        {
            for(int j=0; j<C; j++)
            {
                cin>>x;
                k[i][j]=x;
                if(x!='?')
                    P.push_back(x);

            }
        }


        for(int i=0; i<R; i++)
        {
            char s;
            int y=0,z=0;
            x=k[i][0];
            while(x=='?' && y<C)
            {
                y++;
                x=k[i][y];
            }
            if(y<C)
            {
                for(int j=0; j<y; j++)
                    k[i][j]=x;
                s=x;
                z=y+1;
                while(z<C)
                {
                    while(k[i][z]=='?' and z<C)
                    {
                        k[i][z]=s;
                        z++;
                    }
                    s=k[i][z];
                    z++;
                }

            }



        }
        for(int i=0; i<R; i++)
        {
            int l=i;
            if(i==0 && k[i][0]=='?')
            {

                while(k[l][0]=='?')
                    l++;
                for(int j=0; j<C; j++)
                {
                    for(int h=0; h<l; h++)
                        k[h][j]=k[l][j];
                }
            }
            else if (k[i][0]=='?')
            {
                while(k[l][0]=='?')
                    l--;
                for(int j=0; j<C; j++)
                    k[i][j]=k[l][j];
            }
        }


        cout << "Case #" << t << ": "<<endl;
        for(int i=0; i<R; i++)
        {
            for(int j=0; j<C; j++)
            {
                cout<<k[i][j];
            }
            cout<<endl;
        }
        cout<<endl;
	}
    return 0;
}
