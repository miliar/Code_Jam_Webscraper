DEBUG = False
#DEBUG = True

def print_res(case, ma, mi):
  print("Case #{}: {} {}".format(case, ma, mi))


T = int(input())

for t in range(1, T + 1):
  N, K = [int(x) for x in input().split()]

  if N == K:
    ma = mi = 0
  # elif K > N // 2 and K != 2 ** K.bit_length() - 1:
  #   ma = mi = 0
  elif K == 1:
    chunk_size = N - 1
    ma = chunk_size // 2 + chunk_size % 2
    mi = chunk_size - ma
  else:
    cpo2 = K.bit_length() - 1
    cpo2_value = pow(2, cpo2) - 1

    if K == cpo2_value:
      cpo2_value //= 2

    chunk_size = (N - cpo2_value) // (cpo2_value + 1)

    number_of_bigger_chunks = (N - cpo2_value) % (cpo2_value + 1)

    if number_of_bigger_chunks > 0 and K <= cpo2_value + number_of_bigger_chunks:
      chunk_size += 1

    if DEBUG:
      print("")
      print("{}, {}".format(N, K))
      print("cpo2: {}".format(cpo2))
      print("cpo2_value: {}".format(cpo2_value))
      print("chunk_size: {}".format(chunk_size))
      print("number_of_bigger_chunks: {}".format(number_of_bigger_chunks))

    chunk_size -= 1

    ma = chunk_size // 2 + chunk_size % 2
    mi = chunk_size - ma

  print_res(t, ma, mi)
