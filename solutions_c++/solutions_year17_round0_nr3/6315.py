#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <deque>
#include <cmath>

static long long get_rec(long long N, long long K)
{
  if (K == 1)
    return N - 1;
  else
  {
    if (!(K % 2))
      return get_rec(N / 2, K / 2);
    else
    {
      if (!(N % 2))
	return get_rec(N / 2 - 1, K / 2);
      else
	return get_rec(N / 2, K / 2);
    }
  }
}

static std::tuple< long long, long long> get_min_max(std::string line)
{
  long long N = stoi(line.substr(0, line.find(' ')));
  long long K = stoi(line.substr(line.find(' '), line.find('\n')));

  if (K >= N)
    return std::make_tuple(0, 0);

  long long ret = get_rec(N, K);
  if (ret % 2 == 1)
    return std::make_pair((ret + 1) / 2, (ret - 1) / 2);
  if (!(ret % 2))
    return std::make_pair(ret / 2, ret / 2);
}

static void read_file(char* argv)
{
  std::ifstream in(argv);
  std::ofstream out("output.out");
  std::string line = "";
  long long i = 1;
  std::getline(in, line);
  while (std::getline(in, line))
  {
    std::tuple< long long, long long> t = get_min_max(line);
    out << "Case #" << i << ": " << std::get<0>(t) << ' ' << std::get<1>(t) << std::endl;
    i++;
  }
  in.close();
  out.close();
}

int main(int argc, char* argv[])
{
  if (argc != 2)
    exit(1);
  read_file(argv[1]);
}
