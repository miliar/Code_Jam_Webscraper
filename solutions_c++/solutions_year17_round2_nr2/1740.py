#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <math.h>
#include <climits>
#include <float.h>
using namespace std;

char getMaxChar(int& R, int& Y, int& B)
{
    if (R >= Y && R >= B)
    {
        --R;
        return 'R';
    }
    
    if (Y >= B)
    {
        --Y;
        return 'Y';
    }
    
    --B;
    return 'B';
}

char getMaxCharDiffrentThan(int& R, int& Y, int& B, char lastChar, char firstChar)
{
    if (lastChar == 'R')
    {
        if (firstChar == 'B' && Y == B)
        {
            --B;
            return 'B';
        }
        
        if (Y >= B)
        {
            --Y;
            return 'Y';
        }
        
        --B;
        return 'B';
    }
    
    if (lastChar == 'Y')
    {
        if (firstChar == 'B' && R == B)
        {
            --B;
            return 'B';
        }
        
        if (R >= B)
        {
            --R;
            return 'R';
        }
        
        --B;
        return 'B';
    }
    
    if (firstChar == 'Y' && R == Y)
    {
        --Y;
        return 'Y';
    }
    
    if (R >= Y)
    {
        --R;
        return 'R';
    }
    
    --Y;
    return 'Y';
}

bool solveEasyCase(int R, int Y, int B, string& output)
{
    int initialN = R + Y + B;
    output = "";
    char lastChar = getMaxChar(R, Y, B);
    char firstChar = lastChar;
    
    output += lastChar;
    
    int N = R + Y + B;
    
    for (int i = 0 ; i < N ; ++i)
    {
        lastChar = getMaxCharDiffrentThan(R, Y, B, lastChar, firstChar);
        output += lastChar;
    }
    
    
    if (!(R == 0 && Y == 0 && B == 0))
    {
        output = "IMPOSSIBLE";
        return false;
    }
    
    if (initialN > 1)
    {
        if (output[0] == output[output.size() - 1])
        {
            output = "IMPOSSIBLE";
            return false;
        }
    }
    
    return true;
}

int main() {
    freopen("B-small-attempt4.in", "r", stdin);
    
    int T;
    int N, R, O, Y, G, B, V;
    
    
    
    cin >> T;
    string output;
    
    for (int iteration = 1 ; iteration <= T ; ++iteration)
    {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        
        solveEasyCase(R, Y, B, output);
        
        cout << "Case #" << iteration << ": " << output << endl;
    }
    
    
    return 0;
}
