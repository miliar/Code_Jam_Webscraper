#include <string>
#include <iostream>
#include <queue>

int main()
{
    int test;
    std::cin >> test;

    for(int t = 1; t <= test; t++)
    {
	int n, k;
	std::cin >> n >> k;
	
	std::priority_queue<int> q;
	q.push(n);
	for(int i = 1; i < k; i++)
	{
	    int curr = q.top(); q.pop();
	    
	    //std::cout << curr << std::endl;
	    
	    q.push(curr / 2);
	    q.push((curr - 1) / 2);
	}
	
	std::cout << "Case #" << t << ": " << q.top() / 2 << " " << (q.top() - 1) / 2 << std::endl;
    }
    
    return 0;
}
