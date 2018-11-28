#include<iostream>
#include<fstream>
#include<string>

using namespace std;

void flip( string& p, int index, int K )
{
    while( K-- )
    {
        if( p[index] == '+' )
        {
            p[index] = '-';
        }
        else
        {
            p[index] = '+';
        }
        index++;
    }
}

int solve( string p, int K )
{
    int flips = 0;
    int index = 0;
    while( index < p.length() - (K-1) )
    {
        if( p[index] == '-' )
        {
            flip( p, index, K );
            flips++;
        }
        index++;
    }
    while( index < p.length() )
    {
        if( p[index] == '-' )
            return -1;
        index++;
    }
    return flips;
}

int main()
{
    int numLines, cnt, width, res;
    string pancakes;                    
    ifstream file;
    file.open( "A-large.in" );
    ofstream outf( "A-out.txt" );

    file >> numLines;
    cnt = 0;
    while( cnt < numLines )
    {
        file >> pancakes;
        file >> width;
        res = solve( pancakes, width );
        if( res < 0 )
        {
            outf << "CASE #" << ++cnt << ": " << "IMPOSSIBLE"  << endl;
        }
        else
        {
            outf << "CASE #" << ++cnt << ": " << res  << endl;
        }
    }
    
    file.close();
    outf.close();

    return 0;
}
