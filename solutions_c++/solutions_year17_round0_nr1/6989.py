#include <iostream>
#include <string>

int solve(std::string s, int k)
{
    int res = 0, n = s.length();
    
    for(int i = 0; i < n; i++)
	if(s[i] == '-')
	{
	    if(i + k > n)
		return -1;

	    res++;

	    for(int j = 0; j < k; j++)
		s[i + j] = (s[i + j] == '-') ? '+' : '-';
	}

    return res;
}

int main()
{
    int t;
    std::cin >> t;
    
    for(int i = 0; i < t; i++)
    {
	std::string s;
	int k;
	std::cin >> s >> k;

	int res = solve(s, k);

	std::cout << "Case #" << i + 1 << ": ";
	if(res == -1) std::cout << "IMPOSSIBLE";
	else std::cout << res;
	std::cout << std::endl;
    }

    return 0;
}
