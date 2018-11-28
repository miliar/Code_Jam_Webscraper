//
//  main.cpp
//  B
//
//  Created by Volodymyr Polosukhin on 22/04/2017.
//  Copyright © 2017 Volodymyr Polosukhin. All rights reserved.
//

#include <iostream>
#include <string>
#include <algorithm>
#include <tuple>

using namespace std;

enum
{
    RED,
    YELLOW,
    BLUE,
    COLOUR_NUMBER
};

char withSingleToLetter[COLOUR_NUMBER+1] = "RYB";
char withoutToLetter[COLOUR_NUMBER+1] = "GVO";

string solveSmall(int withSingle[COLOUR_NUMBER], int without[COLOUR_NUMBER])
{
    string answer = "";
    
    while (*max_element(withSingle, withSingle+COLOUR_NUMBER))
    {
        tuple < int, bool, int > countColour[COLOUR_NUMBER];
        
        for (int i = 0; i < COLOUR_NUMBER; ++i)
        {
            countColour[i] = make_tuple(withSingle[i], answer.empty() || answer.front() == withSingleToLetter[i], i);
        }
        
        sort(countColour, countColour+COLOUR_NUMBER);
        
        bool found = false;
        
        for (int i = COLOUR_NUMBER - 1; !found && i >= 0 && get<0>(countColour[i]); --i)
        {
            if (answer.empty() || withSingleToLetter[get<2>(countColour[i])] != answer.back())
            {
                answer.push_back(withSingleToLetter[get<2>(countColour[i])]);
                --withSingle[get<2>(countColour[i])];
                
                found = true;
            }
        }
        
        if (!found)
        {
            answer = "IMPOSSIBLE";
            break;
        }
    }
    
    if (answer.size() > 1 && answer.front() == answer.back())
    {
        answer = "IMPOSSIBLE";
    }
    
    return answer;
}

string bf(int withSingle[COLOUR_NUMBER], int without[COLOUR_NUMBER])
{
    string answer = "";
    
    for (int colour = 0; colour < COLOUR_NUMBER; ++colour)
    {
        answer += string(withSingle[colour], withSingleToLetter[colour]);
        answer += string(without[colour], withoutToLetter[colour]);
    }
    
    sort(answer.begin(), answer.end());

    do
    {
        bool correct = true;
        
        for (int i = 0; i < (int)answer.size() && correct; ++i)
        {
            correct &= answer[(i+1)%(int)answer.size()] != answer[i];
        }
        
        if (correct || answer.size() == 1)
        {
            return answer;
        }
    }
    while (next_permutation(answer.begin(), answer.end()));
    
    
    return "IMPOSSIBLE";
}

void generateSmall(int withSingle[COLOUR_NUMBER], int without[COLOUR_NUMBER])
{
    int n = 1 + rand() % 10;
    
    for (int i = 1; i < COLOUR_NUMBER; ++i)
    {
        without[i] = 0;
        withSingle[i] = n ? rand() % n : 0;
        n -= withSingle[i];
    }
    withSingle[0] = n;
    without[0] = 0;
}

void stress()
{
    while(true)
    {
        int withSingle[COLOUR_NUMBER];
        int without[COLOUR_NUMBER];
        
        generateSmall(withSingle, without);
        
        auto i = bf(withSingle, without);
        auto j = solveSmall(withSingle, without);
        
        if ((i == "IMPOSSIBLE") != (j == "IMPOSSIBLE"))
        {
            break;
        }
    }
}

int main(int argc, const char * argv[]) {
    //stress();
    
    freopen("B-small-attempt0.in.txt", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    
//    freopen("B-example.in", "r", stdin);
//    freopen("B-example.out", "w", stdout);

    
//    freopen("A-large.in.txt", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    
    cout.precision(6);
    cout.setf(ios::fixed);
    
    int t;
    cin >> t;
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        
        int withSingle[COLOUR_NUMBER] = { r, y, b };
        int without[COLOUR_NUMBER] = {g, v, o};
        
        cout << "Case #" << testcase << ": " << solveSmall(withSingle, without) << endl;
    }
    
    return 0;
}
