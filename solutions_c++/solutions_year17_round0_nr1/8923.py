#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <cassert>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

int getSolution(string s, int k);
int getFromIndex(const string &s, int k);
std::string maneuver(const std::string &stack, int from_index, int n);
bool check_for_happy_sides(const std::string &stack);

std::map<char, char> sides ({ {'-', '+'}, {'+', '-'}});


int main(int argc, char *argv[])
{
    int NUM_LINES;
    string STACK;
    int K;
    cin >> NUM_LINES;
    for(int i = 1; i <= NUM_LINES; ++i)
    {
        cin >> STACK;
        cin >> K;

        cout << "Case #" << i << ": " << STACK << " " << K << endl;
        int result = getSolution(STACK, K);

        cout << "Case #" << i << ": ";
        if(result < 0)
            cout << "IMPOSSIBLE";
        else
            cout << result;
        cout << endl;
    }

    return 0;
}

int getSolution(std::string s, int k)
{
    assert(s.length() > 0);
    assert(k >= 2);
    assert(k <= s.length());

    int flips = 0;

    while(!check_for_happy_sides(s))
    {
        // finding next item
        int from = getFromIndex(s, k);
        if(from < 0)
        {
            return -1;
        }

        s = maneuver(s, from, k);
        flips++;
    }

    return flips;
}

int getFromIndex(const std::string &s, int k)
{
    // we need to find the most efficient flip that will turn most of the pancakes
    int from_left = s.find_first_of('-') >= 0 ? s.find_first_of('-') : 0;

    int n_left = s.find_first_of('+', from_left);
    int n_right = s.find_last_of('+', from_left);

    if(n_left < 0 && n_right < 0)
    {
        return s.length() % k != 0 ? -1 : 0;
    }
    else if(n_left == n_right)
        return n_left - 1;

    if(s.length() - from_left < k)
        return -1;

    if(n_left >= k)
        return from_left;
    else if (s.length() - n_right >= k)
        return from_left;
    else
        cout << "not sure what to do with : " << s << " and k=" << k << endl;
    return -1
}

std::string maneuver(const std::string &stack, int from_index, int k)
{
    std::cout<<"flipping " << k << " pancake(s) from " << from_index << " in: " << stack << std::endl;
    assert(k > 0);
    assert(k <= stack.length());
    assert(from_index >= 0);
    assert(stack.length() - k >= from_index);

    std::string resultStack;

    int k_index = from_index + k - 1;
    if(from_index > 0)
    {
        for(int i = 0; i < from_index; ++i)
            resultStack += stack[i];
    }

    for(int i = from_index; i <= k_index; ++i)
        resultStack += sides[stack[i]];

    if(k_index + 1 < stack.length())
    {
        for(int i = k_index + 1; i < stack.length(); ++i)
            resultStack += stack[i];
    }

    std::cout<<"flipped " << k << " pancake(s) and got: " << resultStack << std::endl;
    assert(stack.length() == resultStack.length());

    return resultStack;
}

bool check_for_happy_sides(const std::string &stack)
{
    return stack.find_first_not_of('+') == std::string::npos;
}


