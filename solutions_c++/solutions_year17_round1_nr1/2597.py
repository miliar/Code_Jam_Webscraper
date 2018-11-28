#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
using namespace std;


 vector < vector <char> > fillif( vector < vector <char> > cake)
 {
     set <int> res;
     for(int x =1;x<cake.size();x++)
        if(cake[x][0]=='?')
            cake[x] = cake[x-1];

     for(int x =cake.size()-2;x>=0;x--)
        if(cake[x][0]=='?')
            cake[x] = cake[x+1];


     return cake;





 }

string Getcake( vector < vector <char> > cake)
{


    char fill = '?';
    for(auto &row : cake)
      {
        fill = '?';
        for(auto &piece : row)
        {
            if(piece=='?')
                piece = fill;
            else fill = piece;

        }
    }


    for(int x =cake.size()-1;x>=0;x--)
       {
        fill = '?';
        for(int y =cake[x].size()-1;y>=0;y--)
        {
            if(y==cake[x].size()-1)
                fill = cake[x][y];

            if(cake[x][y]=='?') cake[x][y] = fill;
            else fill = cake[x][y];
        }
    }


  cake =    fillif(cake);


    for(int x =0;x<cake.size();x++)
        for(int y =0;y<cake[x].size();y++)
        {
            if(y==0)cout << "\n";
            cout << cake[x][y];

        }
    cout << "\n";




    return " ";







}

int main(int argc, char *argv[])
{

    int tc;cin >>tc;

    vector < vector <char> > cake;
    vector <char> tcake;

    char temp;

    for(int i=1;i<=tc;i++)
    {

        int r,c;
        cin >> r>>c;
        for(int j=0;j<r;j++)
        for(int k=0;k<c;k++)
        {
            cin >> temp;
            tcake.push_back(temp);
            if(k==c-1)
            {
                cake.push_back(tcake);
                tcake.clear();
            }
        }




        cout << "Case #"<<i<<": ";
        Getcake(cake);
        cake.clear();
    }



  //  int yy;cin >> yy;

    return 0;
}


