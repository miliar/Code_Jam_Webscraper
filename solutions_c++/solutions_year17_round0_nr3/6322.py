#include <iostream>
#include <fstream>
#include <string>
#include <queue>

static void take(unsigned long long n, unsigned long long& min,
		 unsigned long long& max)
{
  if (n == 1)
    min = max = 0;
  else
    min = (max = n / 2) - (n % 2 == 0);
}

static void place(unsigned long long n, unsigned long long k,
		  unsigned long long& min, unsigned long long& max)
{
  std::priority_queue<unsigned long long> queue;
  queue.push(n);
  for (unsigned long long i = 1; i <= k; i++)
    {
      take(queue.top(), min, max);
      queue.pop();
      queue.push(min);
      queue.push(max);
    }
}

int main(int argc, char *argv[])
{
  if (argc != 2)
    return 1;
  std::ifstream in(argv[1]);
  std::ofstream out("output_c");
  std::string token;
  in >> token;
  int t = std::stoi(token);
  for (int row_idx = 1; row_idx <= t; row_idx++)
    {
      out << "Case #" << row_idx << ": ";
      std::string str_n;
      in >> str_n;
      std::string str_k;
      in >> str_k;
      unsigned long long n = std::stoull(str_n);
      unsigned long long k = std::stoull(str_k);
      // BEGIN
      unsigned long long min = 0;
      unsigned long long max = 0;
      place(n, k, min, max);
      out << max << " " << min << std::endl;
      // END
    }
  return 0;
}
