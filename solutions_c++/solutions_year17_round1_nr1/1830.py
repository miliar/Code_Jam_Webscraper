#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    for(int i = 0; i<test; i++)
    {
        int row, col;
        cin>>row>>col;
        char block[30][30];
        for(int j = 0; j<row; j++){
            for(int k = 0; k<col; k++){
                cin>>block[j][k];
            }
        }
        for(int j = 0; j<row; j++)
        {
            for(int k = 0; k<col; k++)
            {
                if(block[j][k]!='?')
                {
                    for(int le = k + 1; le<col; le++)
                        if(block[j][le] == '?')
                            block[j][le] = block[j][k];
                        else
                            break;
                    for(int le = k - 1; le>=0; le--)
                        if(block[j][le] == '?')
                            block[j][le] = block[j][k];
                        else
                            break;
                }
            }
        }
        for(int j = 0; j<(row - 1); j++)
        {
            for(int k = 0; k<col; k++)
                if(block[j][k] != '?' and block[j + 1][k] == '?')
                    block[j + 1][k] = block[j][k];
        }
        for(int j = row - 1; j>0; j--)
        {
            for(int k = 0; k<col; k++)
                if(block[j][k] != '?' and block[j - 1][k] == '?')
                    block[j - 1][k] = block[j][k];
        }
        cout<<"Case #"<<i + 1<<":"<<endl;
        for(int j = 0; j<row; j++)
        {
            for(int k = 0; k<col; k++)
                cout<<block[j][k];
            cout<<endl;
        }
    }
}
