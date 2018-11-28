#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>

static int
getFlips(const std::vector<int>& sequence, int k)
{
  const int bit = 1;
  int sum = 0;
  int result = 0;
  int total = static_cast<int>(sequence.size());

  std::vector<int> s(total, 0);

  for (int i = 0; i < total; ++i)
  {
    s[i] = (sequence[i] + sum) % 2 != bit;
    sum += s[i] - (i >= k - 1 ? s[i - k + 1] : 0);
    result += s[i];

    if ((i > total - k) && (s[i] != 0))
      return std::numeric_limits<int>::max();
  }

  return result;
}

static void
parseLine(const std::string& line, std::vector<int>& sequence, size_t& k)
{
  std::stringstream stream(line);
  std::string ts;
  std::string tk;
  std::getline(stream, ts, ' ');
  std::getline(stream, tk, ' ');

  sequence.reserve(ts.size());

  for (auto i : ts)
    sequence.push_back(i == '+' ? 1 : 0);

  k = std::stoi(tk);
}

static std::string
processLine(const std::string& line)
{
  std::vector<int> sequence;
  size_t k = 0;

  parseLine(line, sequence, k);

  int result = getFlips(sequence, k);

  return result != std::numeric_limits<int>::max() ? std::to_string(result) : "IMPOSSIBLE";
}

int
main(int argc, char** argv)
{
  std::string line;
  std::getline(std::cin, line);

  size_t t = std::stoi(line);

  for (size_t i = 1; i <= t; ++i)
  {
    std::getline(std::cin, line);
    std::cout << "Case #" << i << ": " << processLine(line) << std::endl;
  }

  return 0;
}
